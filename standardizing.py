from traintrack import *
from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *



#train must be standard traintrack
def standardizing_braid(train, fold_here_cusp, direction):
    train_ROL = train.deepcopy()
    train_LOR = train.deepcopy()
    cusp_index = train.cusps.index(fold_here_cusp)

    marked_polygons = train.infpoly["marked"]
    just_the_polygons = []
    for i in marked_polygons:
        just_the_polygons.append(i[1])

    side_swappers_in_order = train.side_swapping_edges

    current_ordered_marked_polygons = [] #a list of list (of vertices in cc order), in order from left to right of the marked polys in the current embedding
    p = 0
    while p < len(marked_polygons):
        for m in just_the_polygons:
            if side_swappers_in_order[p][0] in m:
                current_ordered_marked_polygons.append(m)
        p += 1 



    G = train.graph
    cusp_vertex = fold_here_cusp.vertex
    left_vertex = fold_here_cusp.left_vertex()
    right_vertex = fold_here_cusp.right_vertex()

    original_order = train.vert_orders.copy()

    ##the following determines the intermediate vertex
    if direction == 0: ## right over left
        intermediate_vertex = left_vertex
    else: ##left over right
        intermediate_vertex = right_vertex

    order_intermediate_vertex = original_order[intermediate_vertex] #the ordering of the edges incedent to the intermediate vertex

    #the following determines inf_edge, the infinitesmal edge that the folding will go over
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
        added_edge = tuple(sorted(list((right_vertex, far_vertex))))

    else: #if we are folding left over right
        position = order_intermediate_vertex.index(fold_here_cusp.right)
        if position == 0:
            jIndex = (position - 1) % len(order_intermediate_vertex)
            inf_edge = order_intermediate_vertex[jIndex]
        else:
            inf_edge = order_intermediate_vertex[position - 1]
        #This specifies the far vertex
        if inf_edge[0] == right_vertex:
            far_vertex = inf_edge[1]
        else:
            far_vertex = inf_edge[0]
        added_edge = tuple(sorted(list((left_vertex, far_vertex))))

    
    train_ROL.fold(train_ROL.cusps[cusp_index],0)
    train_LOR.fold(train_LOR.cusps[cusp_index],1)

    if direction == 0:
        folded_train = train_ROL
    else:
        folded_train = train_LOR



    order_of_far_vertex = folded_train.vert_orders[far_vertex]
    index_of_inf_edge = order_of_far_vertex.index(inf_edge)
    inf_edge_is_at_the_end = False
    inf_edge_is_at_the_beginning = False
    swing_left = False
    swing_right = False
    index_of_added_edge = order_of_far_vertex.index(added_edge)


    if index_of_inf_edge == len(order_of_far_vertex) - 1:
        inf_edge_is_at_the_end = True
        if index_of_added_edge == 0:
             swing_right = True
        elif index_of_inf_edge - index_of_added_edge == 1:
             swing_left = True
    elif index_of_inf_edge == 0:
        inf_edge_is_at_the_beginning = True
        if index_of_added_edge == 1:
             swing_right = True
        elif index_of_added_edge == len(order_of_far_vertex) - 1:
             swing_left = True
    else: 
        index_difference = index_of_inf_edge - index_of_added_edge
        if index_difference == -1:
             swing_right = True
        elif index_difference == 1:
             swing_left = True
         


    if inf_edge not in side_swappers_in_order:  # if folding does not go over a side-swapping edge, then standardizing braid is the empty braid
        return None
    elif swing_left == True:
        offending_position = side_swappers_in_order.index(inf_edge)  # m - 1, if it's the first one form the left it's 0 
        for side_swapper_to_the_right in side_swappers_in_order[offending_position+1:]:
            associated_infpoly = current_ordered_marked_polygons[side_swappers_in_order.index(side_swapper_to_the_right)]
            for vertex in associated_infpoly:
                all_paths_far_vert_to_vertex = folded_train.graph.all_paths(far_vertex, vertex, report_edges=True)
                if is_edge_among_paths(all_paths_far_vert_to_vertex, added_edge) == True: 
                    where_to_end = side_swappers_in_order.index(side_swapper_to_the_right)
        return f"delta^(-1)_[{offending_position + 1},{where_to_end}]"
    
    elif swing_right == True:
        offending_position = side_swappers_in_order.index(inf_edge)  # m - 1, if it's the first one form the left it's 0 
        for side_swapper_to_the_left in side_swappers_in_order[offending_position-1::-1]:
            associated_infpoly = current_ordered_marked_polygons[side_swappers_in_order.index(side_swapper_to_the_left)]
            for vertex in associated_infpoly:
                all_paths_far_vert_to_vertex = folded_train.graph.all_paths(far_vertex, vertex, report_edges=True)
                if is_edge_among_paths(all_paths_far_vert_to_vertex, added_edge) == True: 
                    where_to_end = side_swappers_in_order.index(side_swapper_to_the_left)
        return f"delta_[{offending_position + 1},{where_to_end}]"
                




def is_edge_among_paths(all_paths, edge): #all_paths is a list of paths, each path is a list of edges
    for path in all_paths:
        sorted_path = [tuple(sorted(list(t))) for t in path]
        if tuple(sorted(list(edge))) in sorted_path:
            return True
    return False
         
         

            
