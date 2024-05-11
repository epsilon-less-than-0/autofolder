from sage.graphs.views import EdgesView
import cusp
class traintrack:
    def __init__(self, graph, cusps, vertex_edges_ordering):
        self.graph = graph
        self.cusps = cusps
        #self.infpoly = infpoly
        self.vert_orders = vertex_edges_ordering

    ## graph as a Sagemath graph
    ## cusps as a list of objects of class cusp, only cusps made by two real edges allowed
    ## inf poly is a list of infinitesimal polygons, each infinitesimal polygon is a list of vertices, ordered counterclockwise
    ## vertex_edges_ordering is a dictionary, where the key is a vertex, as an integer, 
    ## and the value is a list of indicent edges (an edge is an ordered tuple) ordered counterclockwise 

    def in_poly(self,vertex): ## Checks if a vertex is in an infinitesimal polygon or not
        v = vertex
        for i in self.infpoly:
            for j in i:
                if j == v:
                    return True
                else:
                    continue
            return False

    def vertex_edges_ordering(self,vertex): ## input is a vertex, outputs a list of incident edges, ordered counterclockwise
        return self.vert_orders[vertex]

    def delete_cusp(self,cusp): # input is a cusp, in the form of an object of class cusp
        c = cusp
        self.cusps.remove(c)
        return self
    
    def add_cusp(self,cusp):
        c = cusp
        self.cusps.append(c)
        return self

    def fold(self,cusp,direction): #direction is 0 if right-over-left, 1 if left-over-right
        G = self.graph
        cusp_vertex = cusp.vertex
        left_vertex = cusp.left_vertex()
        right_vertex = cusp.right_vertex()
        vertices = G.vertices(sort = True)
        star_vertex = len(vertices)
        G.add_vertices([star_vertex])
        G.add_edges([(star_vertex, left_vertex), (star_vertex,right_vertex), (star_vertex, cusp_vertex)])
        G.delete_edges([(cusp_vertex,left_vertex),(cusp_vertex,right_vertex)])
        if direction == 0: ## right over left
            G.contract_edge(left_vertex,star_vertex) #contract star_vertex into left_vertex
            intermediate_vertex = left_vertex
        else: ##left over right
            G.contract_edge(right_vertex,star_vertex) #contract star_vertex into right_vertex
            intermediate_vertex = right_vertex

        order_intermediate_vertex = self.vertex_edges_ordering(intermediate_vertex) #the ordering of the edges incedent to the intermediate vertex

        if direction == 0: #if we are folding right over left
            position = order_intermediate_vertex.index(cusp.left) #this is the order of the real edge right before the inf edge
            if position == len(order_intermediate_vertex) - 1:
                jIndex = (position + 1) % len(order_intermediate_vertex)
                inf_edge = order_intermediate_vertex[jIndex]
            else:
                inf_edge = order_intermediate_vertex[position + 1] #the inf edge is right after the real edge at position

            #This specifies the far vertex
            if inf_edge[0] == left_vertex:
                far_vertex = inf_edge[1]
            else:
                far_vertex = inf_edge[0]
            
            #Now the third stage, we fold over the inf edge
            G.add_edge(right_vertex, far_vertex)
            added_edge = tuple(sorted(list((right_vertex, far_vertex))))
            G.delete_edge(right_vertex,intermediate_vertex)

            #Now G has been replaced by a folded graph


            #Now we will define the ordering dictionary for the folded graph
            #First we initialize the new ording to be the same as the old ordering
            new_ordering = self.vert_orders

            #Add an edge for far_vertex in the appropriate order
            inf_edge_index = new_ordering[far_vertex].index(inf_edge) #position of inf edge
            new_ordering[far_vertex] = new_ordering[far_vertex].insert(inf_edge_index + 1, tuple(sorted((right_vertex, far_vertex))))

            #Cusp vertex had the right edge removed
            new_ordering[cusp_vertex] = new_ordering[cusp_vertex].remove(cusp.right)

            #right vertex
            index = new_ordering[right_vertex].index(cusp.right)
            new_ordering[right_vertex] = new_ordering[right_vertex].remove(cusp.right)
            new_ordering[right_vertex] = new_ordering[right_vertex].insert(index,tuple(sorted((right_vertex, far_vertex))))

            #intermediate vertex
            new_ordering[intermediate_vertex] = new_ordering[intermediate_vertex].remove(cusp.left)

            #replace the cusp we folded by a new cusp
            self.delete_cusp(cusp)
            self.add_cusp(cusp(far_vertex,[added_edge,tuple(sorted((right_vertex,intermediate_vertex)))]))
        else: #if we are folding left over right
            position = order_intermediate_vertex.index(cusp.right)
            if position == 0:
                jIndex = (position - 1) % len(order_intermediate_vertex)
                inf_edge = order_intermediate_vertex[jIndex]
            else:
                inf_edge = order_intermediate_vertex[position - 1]
            if inf_edge[0] == right_vertex:
                far_vertex = inf_edge[1]
            else:
                far_vertex = inf_edge[0]
            G.add_edge(left_vertex, far_vertex)
            added_edge = tuple(sorted(list((left_vertex, far_vertex))))
            G.delete_edge(left_vertex,intermediate_vertex)
            #Now G has been replaced by a folded graph


            #Now we will define the ordering dictionary for the folded graph
            #First we initialize the new ording to be the same as the old ordering
            new_ordering = self.vert_orders

            #Add an edge for far_vertex in the appropriate order
            inf_edge_index = new_ordering[far_vertex].index(inf_edge) #position of inf edge
            new_ordering[far_vertex] = new_ordering[far_vertex].insert(inf_edge_index - 1, tuple(sorted((left_vertex, far_vertex))))

            #Cusp vertex had the left edge removed
            new_ordering[cusp_vertex] = new_ordering[cusp_vertex].remove(cusp.left)

            #left vertex
            index = new_ordering[left_vertex].index(cusp.left)
            new_ordering[left_vertex] = new_ordering[left_vertex].remove(cusp.left)
            new_ordering[left_vertex] = new_ordering[left_vertex].insert(index,tuple(sorted((left_vertex, far_vertex))))

            #intermediate vertex
            new_ordering[intermediate_vertex] = new_ordering[intermediate_vertex].remove(cusp.right)

            #replace the cusp we folded by a new cusp
            self.delete_cusp(cusp)
            self.add_cusp(cusp(far_vertex,[tuple(sorted(left_vertex,far_vertex)),f]))
                          
        return traintrack(G,self.cusp, self.cusps, new_ordering)
    

    def is_isomorphic_to(self, another_track):
        G = self.graph
        H = another_track.graph
        Graph = True
        Cusps = True
        #Inf = True
        Ord = True
        if G.is_isomorphic(H):
            print("graphs are isomorphic")
        else:
            print("graphs are NOT isomorphic")
            Graph = false
        if self.cusps == another_track.cusps:
            print("cusp info are the same")
        else:
            print("cusp info are NOT the same")
            Cusps = False
        #if self.infpoly == another_track.infpoly:
            #print("infinitesimal polygons are the same")
        #else:
            #print("infinitesimal polygons are NOT the same")
            #Inf = False
        if self.vert_orders == another_track.vert_orders:
            print("vertex edges orderings are the same")
        else:
            print("vertex edges orderings are NOT the same")
            Ord = False
        if Graph == True and Cusps == True and Ord == True:
            return True 
        else:
            return False
        
