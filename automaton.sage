from traintrack import *
from cusp import *
from sage.graphs.views import EdgesView
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from is_traintrack_in_list import *
from standardizing import *


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
 
print("Dictionary defining the underlyging graph is:", Gdict)

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




T = StandardTrainTrack(G,cusps_list, order, singularity_type, infpoly, side_swapping_edges)



# RIGHT_OVER_LEFT = 0
# LEFT_OVER_RIGHT = 1


AutomatonDict = {0:T} 
AutomatonGraph = DiGraph({0:[]}) #The automaton as a graph
AutomatonGraph.allow_multiple_edges(True)
AutomatonGraph.allow_loops(True)


list_of_tracks = [T] #list of train tracks, index of a traintrack is as specified by AutomatonDict

cusp_dictionary = {0:cusps_list} #key is an integer, associated with a traintrack as specified by AutomatonDict


we_added_new_traintracks = True  # Start with True to enter the loop
number_of_traintrack_counter = 0

while we_added_new_traintracks == True:
    print("we added new tracks")
    we_added_new_traintracks = False  # Set to False initially, will be set to True if anything new is appended
    for j in list_of_tracks[number_of_traintrack_counter:]:
        index_of_cusp = 0
        for i in cusp_dictionary[list_of_tracks.index(j)]:
            print(f'i is {i} and j is {j}')
            print(f'we_added_new_traintracks is {we_added_new_traintracks}')
            T_ROL = j.deepcopy()
            T_ROL.fold(T_ROL.cusps[index_of_cusp], 0)
            T_LOR = j.deepcopy()
            T_LOR.fold(T_LOR.cusps[index_of_cusp], 1)

            print("checking if folded ROL is in the list")
            if is_traintrack_in_list(T_ROL, list_of_tracks)[0] == False: #if folded T_ROL is NOT in list
                print("folded ROL is NOT in the list")
                added_traintrack_index = len(list_of_tracks)
                list_of_tracks.append(T_ROL)
                we_added_new_traintracks = True  # Set to True since a new track is added
                AutomatonGraph.add_vertices([list_of_tracks.index(j),added_traintrack_index])
                AutomatonGraph.add_path((list_of_tracks.index(j),added_traintrack_index))
                AutomatonGraph.set_edge_label(list_of_tracks.index(j),added_traintrack_index, standardizing_braid(j,i,0))
                cusp_dictionary[added_traintrack_index] = T_ROL.cusps
                AutomatonDict[added_traintrack_index] = T_ROL
                number_of_traintrack_counter += 1
            else:
                print("folded ROL is in the list")
                existing_traintrack_index = is_traintrack_in_list(T_ROL, list_of_tracks)[1]
                AutomatonGraph.add_vertices([existing_traintrack_index,existing_traintrack_index])
                AutomatonGraph.add_path((list_of_tracks.index(j),existing_traintrack_index))
                AutomatonGraph.set_edge_label(list_of_tracks.index(j),existing_traintrack_index, standardizing_braid(j,i,0))


            print("checking if folded LOR is in the list")
            if is_traintrack_in_list(T_LOR, list_of_tracks)[0] == False:# if folded T_LOR is NOT in list
                print("folded LOR is NOT in the list")
                added_traintrack_index = len(list_of_tracks)
                list_of_tracks.append(T_LOR)
                we_added_new_traintracks = True  # Set to True since a new track is added
                AutomatonGraph.add_vertices([list_of_tracks.index(j),added_traintrack_index])
                AutomatonGraph.add_path((list_of_tracks.index(j),added_traintrack_index))
                AutomatonGraph.set_edge_label(list_of_tracks.index(j),added_traintrack_index, standardizing_braid(j,i,1))
                cusp_dictionary[added_traintrack_index] = T_LOR.cusps
                AutomatonDict[added_traintrack_index] = T_LOR
                number_of_traintrack_counter += 1
            else:
                print("folded LOR is in the list")
                added_traintrack_index = len(list_of_tracks)
                existing_traintrack_index = is_traintrack_in_list(T_LOR, list_of_tracks)[1]
                AutomatonGraph.add_vertices([existing_traintrack_index,existing_traintrack_index])
                AutomatonGraph.add_path((list_of_tracks.index(j),existing_traintrack_index))
                AutomatonGraph.set_edge_label(list_of_tracks.index(j),existing_traintrack_index, standardizing_braid(j,i,1))
            index_of_cusp += 1

    print(f'i is {i} and j is {j}')
    print(f'we_added_new_traintracks is {we_added_new_traintracks}')

AutomatonGraph.set_vertices(AutomatonDict)

# If we reach here without setting we_added_new_traintracks to True, then no new tracks were added
# and we will exit the loop
        
            


    
    











