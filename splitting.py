from traintrack import *
from realedges import realedges
from find_other_integer import find_other_integer
from cusp import *
from is_traintrack_in_list import *

def t_split(track, vertex, direction):
    real_edges = realedges(track.graph, track.infpoly, labels = False)
    ordering_of_vertex = track.vert_orders[vertex]
    ordering_only_real = []
    for e in ordering_of_vertex:
        if e in real_edges:
            ordering_only_real.append(e)
            
    real_start, real_end = find_real_tuple_group(ordering_of_vertex, ordering_only_real)
    r_v = ordering_of_vertex[real_start]
    l_v = ordering_of_vertex[real_end]
    i_r = ordering_of_vertex[real_start - 1]
    i_l = ordering_of_vertex[real_end + 1 %len(ordering_of_vertex)]
    v_r = find_other_integer(i_r,vertex)
    v_l = find_other_integer(i_l,vertex)

    track_copy = track.deepcopy()

    # if track_copy.graph.allow_multiple_edges == True:

    
    if direction == 'left':
        alpha_zero = find_other_integer(l_v, vertex)
        track_copy.graph.delete_edge(l_v)
        ordering_of_vl = track.vert_orders[v_l]
        ordering_of_vl_only_real = []
        for e in ordering_of_vl:
            if e in real_edges:
                ordering_of_vl_only_real.append(e)
        
        real_start_vl, real_end_vl = find_real_tuple_group(ordering_of_vl, ordering_of_vl_only_real)

        r_vl = ordering_of_vl[real_start_vl]
        alpha = tuple(sorted([alpha_zero, find_other_integer(r_vl,v_l)]))
        track_copy.graph.add_edge(alpha)
        vertex_that_needs_added_order = find_other_integer(r_vl,v_l)
        order_of_vertex_that_needs_added_order = track_copy.vert_orders[vertex_that_needs_added_order]
        index_of_rvl = order_of_vertex_that_needs_added_order.index(r_vl)
        order_of_vertex_that_needs_added_order.insert((index_of_rvl + 1 %len(order_of_vertex_that_needs_added_order)), alpha)
        order_of_vertex = track_copy.vert_orders[vertex]
        order_of_vertex.remove(l_v)


        #new cusp information
        cusps = track_copy.cusps
        index_of_cusp = None
        for c in cusps:
            if c.vertex != vertex:
                continue
            elif c.left == l_v:
                index_of_cusp = cusps.index(c)
                
        
        new_cusp_vertex = vertex_that_needs_added_order
        new_left = alpha
        new_right = order_of_vertex_that_needs_added_order[index_of_rvl %len(order_of_vertex_that_needs_added_order)]
        new_cusp = cusp(new_cusp_vertex, (new_left,new_right))
        cusps[index_of_cusp] = new_cusp

        return track_copy
    
    elif direction == 'right':
        alpha_zero = find_other_integer(r_v, vertex)
        track_copy.graph.delete_edge(r_v)
        ordering_of_vr = track.vert_orders[v_r]
        ordering_of_vr_only_real = []
        for e in ordering_of_vr:
            if e in real_edges:
                ordering_of_vr_only_real.append(e)
                       
        real_start_vr, real_end_vr = find_real_tuple_group(ordering_of_vr, ordering_of_vr_only_real)
        l_vr = ordering_of_vr[real_end_vr]
        alpha = tuple(sorted([alpha_zero, find_other_integer(l_vr,v_r)]))
        track_copy.graph.add_edge(alpha)
        vertex_that_needs_added_order = find_other_integer(l_vr,v_r)
        order_of_vertex_that_needs_added_order = track_copy.vert_orders[vertex_that_needs_added_order]
        index_of_lvr = order_of_vertex_that_needs_added_order.index(l_vr)
        order_of_vertex_that_needs_added_order.insert((index_of_rvl - 1 %len(order_of_vertex_that_needs_added_order)), alpha)
        order_of_vertex = track_copy.vert_orders[vertex]
        order_of_vertex.remove(r_v)


        #new cusp information
        cusps = track_copy.cusps
        index_of_cusp = None
        for c in cusps:
            if c.vertex != vertex:
                continue
            elif c.right == r_v:
                index_of_cusp = cusps.index(c)
                
        
        new_cusp_vertex = vertex_that_needs_added_order
        new_right = alpha
        new_left = order_of_vertex_that_needs_added_order[index_of_lvr %len(order_of_vertex_that_needs_added_order)]
        new_cusp = cusp(new_cusp_vertex, (new_left,new_right))
        cusps[index_of_cusp] = new_cusp

        return track_copy






def splitting_tree(track,jointless_tracks):
    SplittingGraph = DiGraph({0:[]})
    SplittingGraph.allow_multiple_edges(True)
    SplittingGraph.allow_loops(True)

    list_of_tracks = [track]
    current_train_track_index = 0

    vertices_to_split = vertices_for_splitting(track)

    vertices_to_split_dictionary = {0:vertices_to_split}

    if len(vertices_to_split) == 0:
        return None

    while current_train_track_index < len(list_of_tracks):
        j = list_of_tracks[current_train_track_index]
        index_of_vertex = 0

        lsplit_track = t_split(track.deepcopy(), vertices_to_split_dictionary[current_train_track_index][index_of_vertex], 'left')
        rsplit_track = t_split(track.deepcopy(), vertices_to_split_dictionary[current_train_track_index][index_of_vertex], 'right')
        list_of_tracks.append(lsplit_track)
        list_of_tracks.append(rsplit_track)
        SplittingGraph.add_edge(list_of_tracks[current_train_track_index], list_of_tracks.index(lsplit_track))
        SplittingGraph.add_edge(list_of_tracks[current_train_track_index], list_of_tracks.index(rsplit_track))

        
        lsplit_inlist , lsplit_in_jointless_index =  is_traintrack_in_list(lsplit_track, jointless_tracks)
        rsplit_inlist , rsplit_in_jointless_index =  is_traintrack_in_list(rsplit_track, jointless_tracks)


        if lsplit_inlist == True:
            if lsplit_in_jointless_index == jointless_tracks.index(j):
                SplittingGraph.set_edge_label(list_of_tracks[current_train_track_index], list_of_tracks.index(lsplit_track), 'l-split, ')












    







def vertices_for_splitting(track):
#input is a traintrack (doesn't necessarily have to be standard), outputs a list of vertices with
#more than one incident real edge 
    all_vertices = track.graph.vertices()
    vertices_that_can_split = []
    real_edges = realedges(track.graph, track.infpoly, labels = False)
    for v in all_vertices:
        neighbors = track.graph.neighbors(v)
        if len(neighbors) == 0:
            continue
        else:
            ordering = track.vert_orders[v]
            ordering_only_real = []
            for e in ordering:
                if e in real_edges:
                    ordering_only_real.append(e)
        if len(ordering_only_real)>1:
            vertices_that_can_split.append(v)

def find_group_boundaries(tuple_list, real_tuples):
    if not tuple_list:
        return []

    def is_real(t):
        return t in real_tuples

    # Find the first transition
    first_type = is_real(tuple_list[0])
    first_transition = next((i for i, t in enumerate(tuple_list) if is_real(t) != first_type), None)

    if first_transition is None:
        return []  # All tuples are of the same type

    # Check if the list starts with 'infinitesimal' (non-real)
    starts_with_infinitesimal = not first_type

    # Find the second transition
    second_transition = next((i for i in range(first_transition + 1, len(tuple_list)) if is_real(tuple_list[i]) == first_type), None)

    if second_transition is None:
        # Only one transition, return it
        return [first_transition]
    else:
        # Two transitions, return both
        return [first_transition, second_transition]
    

def find_real_tuple_group(tuple_list, real_tuples):
    if not tuple_list:
        return None, None

    def is_real(t):
        return t in real_tuples

    n = len(tuple_list)
    real_count = sum(1 for t in tuple_list if is_real(t))

    if real_count == 0:
        return None, None
    if real_count == n:
        return 0, n - 1

    # Find the first real tuple
    pre_wrap_start = None
    for i in range(n - 1, -1, -1):
        if is_real(tuple_list[i]) and ((not is_real(tuple_list[(i - 1) % n])) or i == 0):
            pre_wrap_start = i%n
            break
    

    end = (pre_wrap_start + (real_count - 1)) % n

    return pre_wrap_start, end

    





