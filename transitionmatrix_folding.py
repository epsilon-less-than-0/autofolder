from traintrack import *
from cusp import *
from sage.graphs.views import EdgesView
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from is_traintrack_in_list import *
from standardizing import *
from convert_delta_to_perm import convert_delta_to_perm
from realedges import realedges
from sage.matrix.constructor import matrix



#this only outputs transition matrix if folded_track and ending_track ARE ISOMORPHIC(in my sense)
#BOTH TRACKS HAVE TO HAVE REAL EDGES LABELLED
#starting_track is folded
#ending_track is existing track in list
#pre_folded_track is pre folded track
#fold_here_cusp is a cusp of PRE_FOLDED_TRACK


def transitionmatrix_folding(starting_track, ending_track, fold_here_cusp, direction, pre_folded_track): 
    H = ending_track.graph
    # cusp_index = starting_track.cusps.index(fold_here_cusp)
    ListofRealEdges_starting = realedges(starting_track.graph,starting_track.infpoly)
    ListofRealEdges_ending = realedges(ending_track.graph,ending_track.infpoly)
    

        
    if starting_track.graph.is_isomorphic(H) == False:
        print("the underlying graphs are not the same")
        
        return [False,None]
    else:
        print("the underlying graphs are the same, checking permutations")
        H_edges = EdgesView(ending_track.graph,sort = True, labels = False)
        H_order = ending_track.vert_orders
        singularity_type_marked = starting_track.singularity_type["marked"] #singularity types of the marked singularities, as a list
        singularity_type_marked.sort() 
        singularity_type_marked_ordered_set = list(set(singularity_type_marked)) #singularity types of the marked singularities, as an ordered list with no duplicates
        singularity_type_unmarked = starting_track.singularity_type["unmarked"] #singularity types of the unmarked singularities, as a list
        singularity_type_unmarked.sort()
        singularity_type_unmarked_ordered_set = list(set(singularity_type_unmarked))#singularity types of the unmarked singularities, as a set so no duplicates


        number_of_polygons = len(singularity_type_marked) + len(singularity_type_unmarked) #number of polygons
        print("there are a total %d infinitesimal polygons" % number_of_polygons)
        
        number_of_vertices = len(starting_track.graph.vertices())

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
                    for indic in starting_track.infpoly["marked"]:
                        if indic[0] == j:
                            index_start = starting_track.infpoly["marked"].index(indic)
                            break

                    
                    #extracts those polygons from infpoly["marked"] as a list
                    polygons_of_this_type_in_order = starting_track.infpoly["marked"][index_start:index_start+number_of_polygons_of_this_type]
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
                    for indic in starting_track.infpoly["unmarked"]:
                        if indic[0] == n:
                            index_start = starting_track.infpoly["unmarked"].index(indic)
                            break
                    
                    #extracts those polygons from infpoly["unmarked"] as a list
                    polygons_of_this_type_in_order_un = starting_track.infpoly["unmarked"][index_start:index_start+number_of_polygons_of_this_type_un]

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
                        Griefgraph = starting_track.graph.copy()
                        Grief_order = copy.deepcopy(starting_track.vert_orders)

                        #relabel the vertices of G according to which_vertex_is_sent_to_which
                        Griefgraph.relabel(which_vertex_is_sent_to_which)
                        #get the edges of the relabelled graph
                        Grief_edges = EdgesView(Griefgraph, sort = True, labels = False)



                        Grief_order = replace_order(Grief_order, which_vertex_is_sent_to_which)

                        #which_vertex_is_sent_to_which is a dictionary whose keys are the vertices of starting_tracl (folded track), and keys are where 
                        #each of those vertices is sent to in ending_track (existing track in list)

                        if Grief_edges == H_edges and are_dict_values_same_up_to_cyclic_order(Grief_order,H_order) == True:
                            print("the traintracks are isomorphic, the permutation of vertices is the following")
                            print(which_vertex_is_sent_to_which)
                            realedge_label_transition_dictionary = {}

                            for e in ListofRealEdges_starting:
                                e_is_send_to = tuple(sorted(list((which_vertex_is_sent_to_which[e[0]],which_vertex_is_sent_to_which[e[1]]))))
                                realedge_label_transition_dictionary[int(e[2])] = int(ending_track.graph.edge_label(e_is_send_to[0],e_is_send_to[1]))

                            realedge_label_transition_dictionary = dict(sorted(realedge_label_transition_dictionary.items()))
                            transitionmatrix_list_of_rows = create_zero_matrix(len(ListofRealEdges_starting))
                            for column in realedge_label_transition_dictionary.keys():
                                row = realedge_label_transition_dictionary[column]
                                transitionmatrix_list_of_rows[row - 1][column - 1] = 1
                            
                            if direction == 0: #if it's ROL
                                column_to_add = int(pre_folded_track.graph.edge_label(tuple(sorted(list(fold_here_cusp.right)))[0],tuple(sorted(list(fold_here_cusp.right)))[1]))
                                print(f"column to add is {column_to_add}")
                                row_to_add_pre_permute = int(pre_folded_track.graph.edge_label(tuple(sorted(list(fold_here_cusp.left)))[0],tuple(sorted(list(fold_here_cusp.left)))[1]))
                                print(f"row to add pre permute is {row_to_add_pre_permute}")
                                row_to_add = realedge_label_transition_dictionary[row_to_add_pre_permute]
                                print(f"row to add is {row_to_add}")
                            else: #if it's LOR
                                column_to_add = int(pre_folded_track.graph.edge_label(tuple(sorted(list(fold_here_cusp.left)))[0],tuple(sorted(list(fold_here_cusp.left)))[1]))
                                row_to_add_pre_permute = int(pre_folded_track.graph.edge_label(tuple(sorted(list(fold_here_cusp.right)))[0],tuple(sorted(list(fold_here_cusp.right)))[1]))
                                row_to_add = realedge_label_transition_dictionary[row_to_add_pre_permute]

                            transitionmatrix_list_of_rows[row_to_add - 1][column_to_add - 1] = transitionmatrix_list_of_rows[row_to_add - 1][column_to_add - 1] + 1
                            
                            transition_matrix = matrix(transitionmatrix_list_of_rows)

                            return [True,transition_matrix]
            
        return [False,None]
    

def replace_elements_in_tuple(tup, replacements): #replace the entries of a tuple accoridng to the assignement of a dict replacements
    new_tuple = tuple(replacements.get(item, item) for item in tup)
    tup = new_tuple  # Assign the new tuple to the same variable name
    return tup

def create_zero_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]