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
from transition_matrix_NON_isomorphic_after_folding import give_edge_label_non_isomorphic_after_folding
from transitionmatrix_folding import transitionmatrix_folding
from give_canonical_edge_label import give_canonical_edge_label
from give_label_after_folding import give_label_after_folding
from cusp_diff import cusp_diff


def traintrack_constructor(standard = True):
    ##################input the singularity,infpoly, and side-swapping edges info#####################
    singularity_type = {}
    infpoly = {"marked":[],"unmarked":[]}
    side_swapping_edges = []

    number_of_marked_points = int(input("Enter the number of marked points: "))
    marked = input("List the singularity types of the marked points as a list, from left to right: ")
    marked_singularity_type = []
    i = 1
    while i < len(marked):
        sing = int(marked[i])
        marked_singularity_type.append(sing)
        infpoly["marked"].append(tuple([sing]))
        i += 2

    singularity_type["marked"] = marked_singularity_type

    for j in range(number_of_marked_points):
        marpolygon = input("Starting from left to right, consider the %dth marked point, which has the singularity type %d. In counterclockwise order, enter the vertices that enclose this marked point as a list: " %(j+1,singularity_type["marked"][j]))
        side_swapper = input("Enter the side-swapping edge for this marked polygon as a tuple: ")
        i = 1
        while i < len(marpolygon):
            vertex = int(marpolygon[i])
            infpoly["marked"][j] = infpoly["marked"][j] + tuple([[]])
            infpoly["marked"][j][1].append(vertex)
            side_swapper = tuple(sorted([int(side_swapper[1]), int(side_swapper[3])]))
            side_swapping_edges.append(side_swapper)
            i += 2


    number_of_unmarked_points = int(input("Enter the number of unmarked singularities: "))
    if number_of_unmarked_points != 0:
        unmarked = input("List the singularity types of the unmarked points as a list: ")
        unmarked_singularity_type = []
        i = 1
        while i < len(unmarked):
            sing = int(unmarked[i])
            unmarked_singularity_type.append(sing)
            infpoly["unmarked"].append(tuple([sing]))
            i += 2

        singularity_type["unmarked"] = unmarked_singularity_type

        for j in range(number_of_unmarked_points):
            unmarpolygon = input("Consider the %dth unmarked singularity, which has the singularity type %d. In counterclockwise order, enter the vertices that enclose this unmarked singularity as a list: " %(j+1,singularity_type["unmarked"][j]))
            i = 1
            while i < len(unmarpolygon):
                vertexi = int(unmarpolygon[i])
                infpoly["unmarked"][j] = infpoly["unmarked"][j] + tuple([[]])
                infpoly["unmarked"][j][1].append(vertexi)
                i += 2
    else:
        unmarked_singularity_type = []

    singularity_type["unmarked"] = unmarked_singularity_type
        

    boundary = input("Enter the singularity type of the boundary (this should be a single integer): ")
    singularity_type["boundary"] = [int(boundary)]



    ##################input the underlying graph, and assemble vertex ordering information#####################
    Gdict = {} #dictionary defining the underlying graph
    order = {}
    
    num_vertices = int(input("Enter the number of vertices of the underlying graph: "))
    
    for vertex_of_graph in range(num_vertices):
        num_connected_vertices = int(input("Consider the vertex numbered %d. How many vertices are connected to this vertex (counting itself if it is a closed vertex)? " %vertex_of_graph))
        list_of_connected_vertices = input("List the vertices connected to this vertex as a list, in counterclockwise order: ")
        connected_vertices_in_order = [] #list of vertices adjacent to vertex_of_graph, in counterclockwise order
        length_of_string = len(list_of_connected_vertices)
        j = 1
        while j < length_of_string:
            adjacent_vertex = int(list_of_connected_vertices[j])
            connected_vertices_in_order.append(adjacent_vertex)
            j += 2

        Gdict[vertex_of_graph] = connected_vertices_in_order

        order[vertex_of_graph] = []
        for k in connected_vertices_in_order:
            order[vertex_of_graph].append(tuple(sorted([vertex_of_graph,k])))


    G = Graph(Gdict)
    
    print("Dictionary defining the underlying graph is:", Gdict)

    ####################input the cusp information#################
    cusps_list = []

    num_cusps = int(input("Enter the number of cusps, only cusps between real edges: "))

    for i in range(num_cusps):
        key = input("Enter a vertex of a cusp: ")
        left = input("Enter the left edge: ")
        right = input("Enter the right edge: ")
        left_edge = tuple(sorted([int(left[1]),int(left[3])]))
        right_edge = tuple(sorted([int(right[1]),int(right[3])]))
        cusps_list.append(cusp(int(key),(left_edge,right_edge)))

    # print("Cusp info: ", cusp)




    if standard == False:
        T = StandardTrainTrack(G,cusps_list, order, singularity_type, infpoly)
        return T
    else:
        for i in range(number_of_marked_points):
            side_swap_input = input(f"Enter the {i}th side swapping edge as a an ordered tuple")
            lefte = int(side_swap_input[1])
            righte = int(side_swap_input[3])
            edge = tuple(sorted([lefte,righte]))
            side_swapping_edges.append(edge)
        
        T = StandardTrainTrack(G,cusps_list, order, singularity_type, infpoly, side_swapping_edges)
        return T