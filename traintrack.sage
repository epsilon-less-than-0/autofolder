from sage.graphs.views import EdgesView
import cusp
class traintrack:
    def __init__(self, graph, cusps, infpoly, vertex_edges_ordering):
        self.graph = graph
        self.cusps = cusps
        self.infpoly = infpoly
        self.vert_orders = vertex_edges_ordering
    ## graph as a Sagemath graph
    ## cusps as a list of objects of class cusp, only cusps made by two real edges allowed
    ## inf poly is a list of infinitesimal polygons, each infinitesimal polygon is a list of vertices, ordered counterclockwise
    ## vertex_edges_ordering is a list of 2-tuples, each 2-tuple's zeroth entry is a vertex, and the first entry is a list of indicent edges ordered counterclockwise 

    def in_poly(self,vertex): ## Checks if a vertex is in an infinitesimal polygon or not
        v = vertex
        for i in self.infpoly:
            for j in i:
                if j == v:
                    return True
                else:
                    continue
            return False

    def vertex_edges_ordering(self,vertex): ## input a vertex, outputs a list of incident edges, ordered counterclockwise
        v = vertex
        for i in self.vert_orders:
            if v == i[0]:
                return i[1]
            else:
                continue

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
        else:
            G.contract_edge(right_vertex,star_vertex) #contract star_vertex into right_vertex
            intermediate_vertex = right_vertex

        order_intermediate_vertex = self.vertex_edges_ordering(intermediate_vertex)

        if direction == 0:
            position = order_intermediate_vertex.index(cusp.left)
            if position == len(order_intermediate_vertex) - 1:
                jIndex = (position - 1) % len(order_intermediate_vertex)
                inf_edge = order_intermediate_vertex[jIndex]
            else:
                inf_edge = order_intermediate_vertex[position + 1]

            if inf_edge[0] == left_vertex:
                far_vertex = inf_edge[1]
            else:
                far_vertex = inf_edge[0]
            G.add_edge(left_vertex, far_vertex)
            G.delete_edge(right_vertex,left_vertex)
        else:
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
            G.delete_edge(left_vertex,right_vertex)

        return traintrack(G,)
        
        
        

        

        

        return traintrack(G,)

