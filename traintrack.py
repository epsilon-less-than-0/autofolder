from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from standardizing import *


class traintrack:
    def __init__(self, graph, cusps, vertex_edges_ordering, singularity_type, infpoly):
        self.graph = graph
        self.cusps = cusps
        self.vert_orders = vertex_edges_ordering
        self.singularity_type = singularity_type
        self.infpoly = infpoly
        
        

    ## graph as a Sagemath graph
    ## cusps as a list of objects of class cusp, only cusps made by two real edges allowed
    ## vertex_edges_ordering is a dictionary, where the key is a vertex, as an integer, 
    ## and the value is a list of indicent edges (an edge is an ordered tuple) ordered counterclockwise 
    ## singularity_type is a dictionary with three keys: "marked", "unmarked", and "boundary". Each value is a list of singularity type information
    ## for example, singularity_type["marked"] = [1,1,1,1] means there are four marked points each a one-pringed singularity
    ## infpoly is a dictionary with two keys: "marked" and "unmarked". The values are each a list. The value for "marked" is a 
    ## list of tuples. Each tuple represents an infinitesimal polygon;
    ## the first entry of the tuple is the singularity as it appears in singularity_type["marked"], and the second entry 
    ## is a list of vertices in counterclockwise order making up the correcponding infinitesimal polygon for that singularity. 
    ## The key for "unmarked" is similar.

    def deepcopy(self):
        return copy.deepcopy(self)

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

    def delete_cusp(self,delete_this_cusp): # input is a cusp, in the form of an object of class cusp
        self.cusps.remove(delete_this_cusp)
        return self
    
    def add_cusp(self,add_this_cusp):
        self.cusps.append(add_this_cusp)
        return self

    def fold(self,fold_here_cusp,direction): #cusp is a cusp object, direction is 0 if right-over-left, 1 if left-over-right
        G = self.graph
        original_graph = G.copy()
        original_order = self.vert_orders.copy()
        G.allow_multiple_edges(True)
        cusp_vertex = fold_here_cusp.vertex
        left_vertex = fold_here_cusp.left_vertex()
        right_vertex = fold_here_cusp.right_vertex()
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

        order_intermediate_vertex = original_order[intermediate_vertex] #the ordering of the edges incedent to the intermediate vertex

        if direction == 0: #if we are folding right over left
            position = order_intermediate_vertex.index(fold_here_cusp.left) #this is the order of the real edge right before the inf edge
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


            #################################################################
            #Now we will define the ordering dictionary for the folded graph#
            #################################################################

            #First we initialize the new ording to be the same as the old ordering (as a copy), and make original a copy of the original ordering as well
            new_ordering = copy.deepcopy(self.vert_orders)
            original = copy.deepcopy(self.vert_orders)

            #Add an edge for far_vertex in the appropriate order
            inf_edge_index = original[far_vertex].index(inf_edge) #position of inf edge
            originally = original[far_vertex].copy()
            originally.insert(inf_edge_index + 1, tuple(sorted((right_vertex, far_vertex))))
            new_ordering[far_vertex] = originally

            #Cusp vertex had the right edge removed
            originallyyyy = original[cusp_vertex].copy()
            originallyyyy.remove(fold_here_cusp.right)
            new_ordering[cusp_vertex] = originallyyyy

            #right vertex
            index = original[right_vertex].index(fold_here_cusp.right)
            originally11 = original[right_vertex].copy()
            originally11.remove(fold_here_cusp.right)
            originally11.insert(index,tuple(sorted((right_vertex, far_vertex))))
            new_ordering[right_vertex] = originally11

            # #intermediate vertex
            # if intermediate_vertex != far_vertex:
            #     originally = original[intermediate_vertex]
            #     new_ordering[intermediate_vertex] = originally.remove(fold_here_cusp.left)

            self.vert_orders = new_ordering

            #####################################
            #replace cusp we folded by a new one#
            #####################################
            far_order = original[far_vertex].copy()
            new_cusp_edge = far_order[inf_edge_index + 1]
            self.delete_cusp(fold_here_cusp)
            self.add_cusp(cusp(far_vertex,[new_cusp_edge,added_edge]))

        else: #if we are folding left over right
            position = order_intermediate_vertex.index(fold_here_cusp.right)
            if position == 0:
                jIndex = (position - 1) % len(order_intermediate_vertex)
                inf_edge = order_intermediate_vertex[jIndex]
            else:
                inf_edge = order_intermediate_vertex[position - 1]
            #the following specifies the far_vertex
            if inf_edge[0] == right_vertex:
                far_vertex = inf_edge[1]
            else:
                far_vertex = inf_edge[0]
            G.add_edge(left_vertex, far_vertex)
            added_edge = tuple(sorted(list((left_vertex, far_vertex))))
            G.delete_edge(left_vertex,intermediate_vertex)
            #Now G has been replaced by a folded graph

            #################################################################
            #Now we will define the ordering dictionary for the folded graph#
            #################################################################
            # print('far_vertex is %d' %far_vertex)
            # print("cusp vertex is %d" %cusp_vertex)
            # print("left_vertex is %d" %left_vertex)
            # print("right_vertex is %d" %right_vertex)
            # print("inf_edge is " )
            # print(inf_edge)
            #First we initialize the new ording to be the same as the old ordering, and make original a copy of the originla ordering
            new_ordering = copy.deepcopy(self.vert_orders)
            original = copy.deepcopy(self.vert_orders)
            #Add an edge for far_vertex in the appropriate order
            inf_edge_index = original[far_vertex].index(inf_edge) #position of inf edge
            originally = original[far_vertex].copy()
            originally.insert(inf_edge_index , tuple(sorted((left_vertex, far_vertex))))
            new_ordering[far_vertex] = originally

            #Cusp vertex had the left edge removed
            originallyy = original[cusp_vertex].copy() #copy ordering of cusp vertex
            originallyy.remove(fold_here_cusp.left) #remove the left edge of cusp
            new_ordering[cusp_vertex] = originallyy


            #left vertex
            index = original[left_vertex].index(fold_here_cusp.left) 
            originally1 = original[left_vertex].copy()
            originally1.remove(fold_here_cusp.left)
            originally1.insert(index,tuple(sorted((left_vertex, far_vertex))))
            new_ordering[left_vertex] = originally1

            # #intermediate vertex
            # if intermediate_vertex != far_vertex:
            #     originallyyy = original[intermediate_vertex].copy()
            #     new_ordering[intermediate_vertex] = originallyyy.remove(fold_here_cusp.right)

            # print("new order is")
            # print(new_ordering)

            self.vert_orders = new_ordering

            #####################################
            #replace cusp we folded by a new one#
            #####################################
            far_order = original[far_vertex].copy()
            new_cusp_edge = far_order[inf_edge_index - 1]
            self.delete_cusp(fold_here_cusp)
            self.add_cusp(cusp(far_vertex,[added_edge,new_cusp_edge]))

        return self
    

    def is_isomorphic_to(self, another_track): #checks isotopy rel set of marked points
        H = another_track.graph
        if self.graph.is_isomorphic(H) == False:
            print("the underlying graphs are not the same")
            return False
        else:
            print("the underlying graphs are the same, checking permutations")
            H_edges = EdgesView(another_track.graph,sort = True)
            H_order = another_track.vert_orders
            singularity_type_marked = self.singularity_type["marked"] #singularity types of the marked singularities, as a list
            singularity_type_marked.sort() 
            singularity_type_marked_ordered_set = list(set(singularity_type_marked)) #singularity types of the marked singularities, as an ordered list with no duplicates
            singularity_type_unmarked = self.singularity_type["unmarked"] #singularity types of the unmarked singularities, as a list
            singularity_type_unmarked.sort()
            singularity_type_unmarked_ordered_set = list(set(singularity_type_unmarked))#singularity types of the unmarked singularities, as a set so no duplicates


            number_of_polygons = len(singularity_type_marked) + len(singularity_type_unmarked) #number of polygons
            print("there are a total %d infinitesimal polygons" % number_of_polygons)
            
            number_of_vertices = len(self.graph.vertices())

            dict_marked_count = {} #dictionary whose kyes are marked singularity types, values are the number of occurance of that singualrity type
            dict_marked_perms = {} #dictionary whose keys are marked singularity types, values are the Sage permutations on the number of occurances of that type
            for i in singularity_type_marked_ordered_set: #fill in dict_marked_count and dict_marked_perms
                dict_marked_count[i] = singularity_type_marked.count(i)
                dict_marked_perms[i] = Permutations(singularity_type_marked.count(i))

            if len(dict_marked_count) == 0:
                print("there are no marked polygons")
            else:
                for q in dict_marked_count:
                    print("there are %d %d-proned marked polygons" %(dict_marked_count[q], q))

            dict_unmarked_count = {} #dictionary whose kyes are unmarked singularity types, values are the number of occurance of that singualrity type
            dict_unmarked_perms = {} #dictionary whose keys are unmarked singularity types, values are the sage permutations permuting those types
            for i in singularity_type_unmarked_ordered_set: #fill in dict_unmarked_count and dict_unmarked_perms
                dict_unmarked_count[i] = singularity_type_unmarked.count(i)
                dict_unmarked_perms[i] = Permutations(singularity_type_unmarked.count(i))

            if len(dict_unmarked_count) == 0:
                print("there are no unmarked/interior polygons")
            else:
                for q in dict_unmarked_count:
                    print("there are %d %d-proned unmarked polygons" %(dict_unmarked_count[q], q))


            # Get the keys and values from the dictionary dict_marked_perms
            keys_marked = list(dict_marked_perms.keys())
            values_marked = list(dict_marked_perms.values())
            list_of_values_marked = [list(value) for value in values_marked]

            # Generate all combinations of values using itertools.product. 
            #This line uses the product function to generate all possible combinations of the values stored in the values list. 
            #The *values syntax is used to unpack the values list into individual arguments to the product function.
            combinations_marked = product(*list_of_values_marked)

            # Convert each combination into a tuple and append it to the result list
            list_of_all_marked_combo_perms = [tuple(comb) for comb in combinations_marked]





            # Get the keys and values from the dictionary dict_unmarked_perms
            keys_unmarked = list(dict_unmarked_perms.keys())
            values_unmarked = list(dict_unmarked_perms.values())
            list_of_values_unmarked = [list(value) for value in values_unmarked]

            # Generate all combinations of values using itertools.product
            combinations_unmarked = product(*list_of_values_unmarked)

            # Convert each combination into a tuple and append it to the result list
            list_of_all_unmarked_combo_perms = [tuple(comb) for comb in combinations_unmarked]


            #internal permutations: each polygon gets its own internal permutation
            internal_permutations_of_marked = []
            internal_permutations_of_unmarked = []
            for h in singularity_type_marked:
                internal_permutations_of_marked.append(Permutations(h))
            for u in singularity_type_unmarked:
                internal_permutations_of_unmarked.append(Permutations(u))
                    
            combinations_internal_marked = product(*internal_permutations_of_marked)
            list_of_all_combinations_internal_marked = [tuple(combb) for combb in  combinations_internal_marked]
            combinations_internal_unmarked = product(*internal_permutations_of_unmarked)
            list_of_all_combinations_internal_unmarked = [tuple(combbv) for combbv in  combinations_internal_unmarked]


            #the following two (nested) for loops fix a choice of permutation for the marked polygons and a permutation for the unmarked polygons
            for i in list_of_all_marked_combo_perms:
                for k in list_of_all_unmarked_combo_perms:
                    # print("checking the marked permutation combo") 
                    # print(i)
                    # print("together with the unmarked permutation combo")
                    # print(k)
                    #after permutations are fixed, initialize which_poly_is_sent_to_which that records polygon pairs (from what sent to what); which_vertex_is_sent_to_which
                    # will be a dictionary with key a vertex and value another vertex that the key is sent to; new_infpoly will be the new infpoly of the permuted traintrack
                    which_poly_is_sent_to_which_marked = []
                    which_poly_is_sent_to_which_unmarked = []
                    which_vertex_is_sent_to_which = {}
                    new_infpoly = {"marked":[], "unmarked":[]}
                    
                    #Now we fill in which_poly_is_sent_to_which_marked, and new_infpoly for marked polys
                    #for each j a marked singularity type,
                    for j in singularity_type_marked_ordered_set:
                        number_of_polygons_of_this_type = dict_marked_count[j] #number of polygons of this type, as an int

                        #this for loop finds the index in infpoly["marked"] at which singularity type j polygons start, stores it in index_start
                        for indic in self.infpoly["marked"]:
                            if indic[0] == j:
                                index_start = self.infpoly["marked"].index(indic)
                                break

                        
                        #extracts those polygons from infpoly["marked"] as a list
                        polygons_of_this_type_in_order = self.infpoly["marked"][index_start:index_start+number_of_polygons_of_this_type]
                        # print("the marked polygons of type %d are these polygons "%j)
                        # print(polygons_of_this_type_in_order)

                        #permute that list of polygons using the chosen permitation i
                        permuted_polygons_in_order = i[singularity_type_marked_ordered_set.index(j)].action(polygons_of_this_type_in_order)
                        # print("the permuted polygons of type %d are these" %j)
                        # print(permuted_polygons_in_order)

                        #add the permuted list of polygons to new_infpoly["marked"]
                        new_infpoly["marked"] = new_infpoly["marked"] + permuted_polygons_in_order

                        #this for loop fills in which_poly_is_sent_to_which for this singularity type
                        for bu in range(number_of_polygons_of_this_type):
                            which_poly_is_sent_to_which_marked.append([polygons_of_this_type_in_order[bu],permuted_polygons_in_order[bu]])
                            # print("which poly is sent to which for marked polygons at the momemnt is")
                            # print(which_poly_is_sent_to_which_marked)


                    #Now we fill in which_poly_is_sent_to_which_unmarked, and new_infpoly for unmarked polys
                    #for each n an unmarked singularity type
                    for n in singularity_type_unmarked_ordered_set:
                        number_of_polygons_of_this_type_un = dict_unmarked_count[n] #number of polygons of this type

                        #this for loop finds the index in infpoly["unmarked"] at which singularity type n polygons start, stores it in index_start
                        for indic in self.infpoly["unmarked"]:
                            if indic[0] == n:
                                index_start = self.infpoly["unmarked"].index(indic)
                                break
                        
                        #extracts those polygons from infpoly["unmarked"] as a list
                        polygons_of_this_type_in_order_un = self.infpoly["unmarked"][index_start:index_start+number_of_polygons_of_this_type_un]

                        #permute that list of polygons using the chosen permitation k
                        permuted_polygons_in_order_un = k[singularity_type_unmarked_ordered_set.index(n)].action(polygons_of_this_type_in_order_un)

                        #add the permuted list of polygons to new_infpoly["unmarked"]
                        new_infpoly["unmarked"] = new_infpoly["unmarked"] + permuted_polygons_in_order_un

                        #this for loop fills in which_poly_is_sent_to_which for this singularity type
                        for zu in range(number_of_polygons_of_this_type_un):
                            which_poly_is_sent_to_which_unmarked.append([polygons_of_this_type_in_order_un[zu],permuted_polygons_in_order_un[zu]])

                    #the following fixes internal permutation combos intermark (for marked) and interunmark (for unmarked), for each polygon we want to permute the vertices
                    for intermark in list_of_all_combinations_internal_marked:
                        markedpolycounter = 0
                        for q in intermark:
                            original_vertices_marked = which_poly_is_sent_to_which_marked[markedpolycounter][0][1]
                            ending_vertices_marked = q.action(which_poly_is_sent_to_which_marked[markedpolycounter][1][1])
                            for b in original_vertices_marked:
                                which_vertex_is_sent_to_which[b] = ending_vertices_marked[original_vertices_marked.index(b)]
                            markedpolycounter = markedpolycounter + 1
                            

                        for interunmark in list_of_all_combinations_internal_unmarked:
                            unmarkedpolycounter = 0
                            for z in interunmark:
                                original_vertices_unmarked = which_poly_is_sent_to_which_unmarked[unmarkedpolycounter][0][1]
                                ending_vertices_unmarked = z.action(which_poly_is_sent_to_which_unmarked[unmarkedpolycounter][1][1])
                                for b in original_vertices_unmarked:
                                    which_vertex_is_sent_to_which[b] = ending_vertices_unmarked[original_vertices_unmarked.index(b)]
                                unmarkedpolycounter = unmarkedpolycounter + 1
                            

                            #copy the original G graph and its order
                            Griefgraph = self.graph.copy()
                            Grief_order = copy.deepcopy(self.vert_orders)

                            #relabel the vertices of G according to which_vertex_is_sent_to_which
                            Griefgraph.relabel(which_vertex_is_sent_to_which)
                            #get the edges of the relabelled graph
                            Grief_edges = EdgesView(Griefgraph, sort = True)



                            Grief_order = replace_order(Grief_order, which_vertex_is_sent_to_which)

                            if Grief_edges == H_edges and are_dict_values_same_up_to_cyclic_order(Grief_order,H_order) == True:
                                print("the traintracks are isomorphic, the permutation of vertices is the following")
                                print(which_vertex_is_sent_to_which)
                                return True
                
            return False
            

            

def replace_elements_in_tuple(tup, replacements): #replace the entries of a tuple accoridng to the assignement of a dict replacements
    new_tuple = tuple(replacements.get(item, item) for item in tup)
    tup = new_tuple  # Assign the new tuple to the same variable name
    return tup

def replace_order(old_order, replacement_vertices_map): #replaces every int in old_order, key or value, by assignment given by replacement_vertices_map
    new_order = {}
    for key, value_list in old_order.items():
        new_key = replacement_vertices_map.get(key, key)
        new_value_list = [tuple(sorted(list((replacement_vertices_map.get(src, src), replacement_vertices_map.get(dest, dest))))) for src, dest in value_list]
        new_order[new_key] = new_value_list
    return new_order
            
            

class StandardTrainTrack(traintrack): #additional side_swapping_edges information is a list, from left right as embedded traintrack
    def __init__(self, graph, cusps, vertex_edges_ordering, singularity_type, infpoly, side_swapping_edges):
        super().__init__(graph, cusps, vertex_edges_ordering, singularity_type, infpoly)
        self.side_swapping_edges = side_swapping_edges



                
            




        
    
        