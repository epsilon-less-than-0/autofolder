from traintrack import *
from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from realedges import realedges
from sage.graphs.connectivity import connected_components_subgraphs
from sage.graphs.connectivity import connected_components



#train must be standard traintrack, the traintrack is BEFORE folding
def standardizing_braid(train, fold_here_cusp, direction):
    train_ROL = train.deepcopy()
    train_LOR = train.deepcopy()
    cusp_index = train.cusps.index(fold_here_cusp)

    marked_polygons = train.infpoly["marked"]
    n = len(marked_polygons)
    #just_the_polygons is a list of marked polygons as they appear in marked_polygons but without the singularity info
    just_the_polygons = []
    for i in marked_polygons:
        just_the_polygons.append(i[1])

    side_swappers_in_order = train.side_swapping_edges

    #current_ordered_marked_polygons
    #is a list of list (of vertices in cc order), in order from left to right of the marked polys in the current embedding,
    #specified by the ordering of side_swappers_in_order
    current_ordered_marked_polygons = [] 
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
        other_vertex = right_vertex

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
        other_vertex = left_vertex

    # if folding does not go over a side-swapping edge, then standardizing braid is the empty braid
    if inf_edge not in side_swappers_in_order:  
        return None

    #perform folding on the traintrack copies 
    train_ROL.fold(train_ROL.cusps[cusp_index],0)
    train_LOR.fold(train_LOR.cusps[cusp_index],1)

    #pick the correct folded train based on direction
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
    real_edges_folded_track = realedges(folded_train.graph,folded_train.infpoly, labels = False)


    #for folded Train track
    marked_polygons_folded = folded_train.infpoly["marked"]
    #just_the_polygons is a list of marked polygons as they appear in marked_polygons but without the singularity info
    just_the_polygons_folded = []
    for i in marked_polygons_folded:
        just_the_polygons_folded.append(i[1])



    #current_ordered_marked_polygons_folded
    #is a list of list (of vertices in cc order), in order from left to right of the marked polys in the current embedding, after folding
    #before standardizing, so side_swappers_in_order is same a before but the polygons might have changed
    #specified by the ordering of side_swappers_in_order
    current_ordered_marked_polygons_folded = [] 
    p = 0
    while p < len(marked_polygons_folded):
        for m in just_the_polygons_folded:
            if side_swappers_in_order[p][0] in m:
                current_ordered_marked_polygons_folded.append(m)
        p += 1 



    #the following part determines if we have almost standard traintrack that is swing left or swing right
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
    

    offending_position = side_swappers_in_order.index(inf_edge)  # if it's the first one form the left it's 0 

         
    #the following part determines if we have wind right or wind left, that is if the offending edge ends to the right or left of the offending position
    wind_left = False
    wind_right = False

    # left_vertex_of_side_swapping = 
    # right_vertex_of_side_swapping = 

    other_poly_position = None
    list_of_all_the_vertices_in_inf_polygon = []
    for pol in just_the_polygons_folded:
        for v in pol:
            list_of_all_the_vertices_in_inf_polygon.append(v)

    if swing_left == True:
        if (other_vertex not in list_of_all_the_vertices_in_inf_polygon):
            wind_left = False
            wind_right = True
        else:
            for poly in current_ordered_marked_polygons_folded:
                if other_vertex in poly:
                    other_poly_position = current_ordered_marked_polygons.index(poly)
            if other_poly_position < offending_position:
                wind_left = True
                wind_right = False
            else:
                wind_left = False
                wind_right = True
    
    if swing_right == True:
        if (other_vertex not in list_of_all_the_vertices_in_inf_polygon):
            wind_left = True
            wind_right = False
        else:
            for poly in current_ordered_marked_polygons_folded:
                if other_vertex in poly:
                    other_poly_position = current_ordered_marked_polygons.index(poly)
            if other_poly_position < offending_position:
                wind_left = True
                wind_right = False
            else:
                wind_left = False
                wind_right = True


    standardizing = None

    if swing_left == True and wind_right == True:
        where_to_end = None
        offending_polygon = current_ordered_marked_polygons_folded[offending_position]
        polygons_to_the_right =  current_ordered_marked_polygons_folded[offending_position+1:] 
        graph_without_added_edge = folded_train.graph.copy()
        graph_without_added_edge.delete_edge(added_edge)
        connected_comps = connected_components(graph_without_added_edge)
        component_with_far_vertex = None
        for component in connected_comps:
            if (far_vertex in component) == True:
                component_with_far_vertex = component
                break

        where_to_end = offending_position
        for polygon in polygons_to_the_right:
            if have_common_element(polygon,component_with_far_vertex) == True:
                where_to_end = where_to_end + 1
            else:
                break

        standardizing = f"delta^(-1)_[{offending_position + 1},{where_to_end + 1}]"
    
    if swing_left == True and wind_left == True:
        where_to_end = None
        offending_polygon = current_ordered_marked_polygons_folded[offending_position]
        ppolygon = offending_polygon
        for side_swapper_to_the_left in side_swappers_in_order[offending_position - 1::-1]:
            associated_infpoly = current_ordered_marked_polygons_folded[side_swappers_in_order.index(side_swapper_to_the_left)]
            if are_infpolys_connected(ppolygon,associated_infpoly,real_edges_folded_track) == False:
                break
            else:
                ppolygon = associated_infpoly
                where_to_end = side_swappers_in_order.index(side_swapper_to_the_left)

        standardizing = f"delta_[{where_to_end + 1},{offending_position + 1}]"
        
    
    if swing_right == True and wind_left == True:
        where_to_end = None
        offending_polygon = current_ordered_marked_polygons_folded[offending_position]
        polygons_to_the_left =  current_ordered_marked_polygons_folded[:offending_position] 
        graph_without_added_edge = folded_train.graph.copy()
        graph_without_added_edge.delete_edge(added_edge)
        connected_comp = connected_components(graph_without_added_edge)
        component_with_far_vertex = None
        for component in connected_comp:
            if (far_vertex in component) == True:
                component_with_far_vertex = component
                break
        
        polygons_to_the_left_reversed = polygons_to_the_left[::-1]
        where_to_end = offending_position
        for polygon in polygons_to_the_left_reversed:
            if have_common_element(polygon,component) == True:
                where_to_end = where_to_end - 1
            else:
                break


        standardizing = f"delta_[{where_to_end + 1},{offending_position + 1}]"

    if swing_right == True and wind_right == True:
        where_to_end = None
        offending_polygon = current_ordered_marked_polygons_folded[offending_position]
        ppolygon = offending_polygon
        for side_swapper_to_the_right in side_swappers_in_order[offending_position+1:]:
            associated_infpoly = current_ordered_marked_polygons_folded[side_swappers_in_order.index(side_swapper_to_the_right)]
            if are_infpolys_connected(ppolygon,associated_infpoly,real_edges_folded_track) == False:
                break
            else:
                ppolygon = associated_infpoly
                where_to_end = side_swappers_in_order.index(side_swapper_to_the_right)

        standardizing = f"delta^(-1)_[{offending_position + 1},{where_to_end + 1}]"

    m = offending_position  + 1
    if is_it_special(standardizing, n, m)[0] == True:
        return is_it_special(standardizing, n, m)[1]
    else:
        return standardizing



def is_it_special(delta, n, m): #check if a standardizing braid is the special type that goes to the end which requires us to choose one
    delta_one_em = f"delta_[1,{m}]"
    delta_inv_m_n = f"delta^{-1}_[{m},{n}]"

    if delta == delta_one_em or delta == delta_inv_m_n:
        return [True, delta_one_em]
    else:
        return [False, None]


def is_edge_among_paths(all_paths, edge): #all_paths is a list of paths, each path is a list of edges
    for path in all_paths:
        sorted_path = [tuple(sorted(list(t))) for t in path]
        if tuple(sorted(list(edge))) in sorted_path:
            return True
    return False


def are_infpolys_connected(inf1,inf2, realedges):
    for real in realedges:
        if real[0] in inf1 and real[1] in inf2:
            return True
        if real[0] in inf2 and real[1] in inf1:
            return True
    return False
         
def have_common_element(list1, list2):
    return bool(set(list1) & set(list2))

            
