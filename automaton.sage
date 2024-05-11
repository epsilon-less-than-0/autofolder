from traintrack import *
from cusp import *


##################input the underlying graph#####################
Gdict = {}
order = {}
 
num_vertices = int(input("Enter the number of vertices of the underlying graph: "))
 
for i in range(num_vertices):
    key = input("Enter vertex: ")
    num_connected_vertices = int(input("How many vertices are connected to this vertex? "))
    list_of_connected_vertices = input("List the vertices connected to this vertex as a list (inside bracket), in counterclockwise order")
    connected_vertices_in_order = []
    length_of_string = len(list_of_connected_vertices)
    j = 1
    while j < length_of_string:
        vert = int(list_of_connected_vertices[j])
        connected_vertices_in_order.append(vert)
        j += 2

    Gdict[int(key)] = connected_vertices_in_order

    for k in connected_vertices_in_order:
        order[int(key)] = tuple(sorted([int(key),k]))


G = Graph(Gdict)
 
print("Dictionary after adding user input:", G)

####################input the cusp information#################
cusp = []

num_cusps = int(input("Enter the number of cusps, only cusps between real edges: "))

for i in range(num_cusps):
    key = input("Enter a vertex of a cusp: ")
    left = input("Enter the left edge: ")
    left_edge = tuple(sorted([int(left[1]),int(right[3])]))
    right = input("Enter the right edge: ")
    right_edge = tuple(sorted([int(right[1]),int(right[3])]))
    cusp.append(cusp(int(key),(left_edge,right_edge)))

print("Cusp info: ", cusp)

###############input the infinitesimal polygon info#####################

#num_monogons = int(input("Enter the number of monogons/marked points: "))
#num_polygons = int(input("Enter the number of non-monogon infinitesimal polygons: "))

#for i in range(num_monogons)


T = traintrack(G,cusp, order)


AutomatonDict = {}

list_of_tracks = [T] #list of train tracks
list_of_folding_maps = {0:[]} # A dictionary recording the folding maps, keys are the indices of a traintrack, value is a list of traintracks it folds to
# at the moment no info other than an arrow to what it folds to

folded_graphs = []

def is_in_list(H,list):
    for i in list:
        if i.is_isomorphic_to(H):
            return True
    return False

for i in G.cusps:
    F0 = G.fold(i,0)
    if is_in_list(F0, list_of_tracks)== False:
        list_of_tracks.append(F0)
        folded_graphs.append(F0)
        list_of_folding_maps[0].append(F0)
    F1 = G.fold(i,1)
    if is_in_list(F1, list_of_tracks)== False:
        list_of_tracks.append(F1)
        folded_graphs.append(F1)
        list_of_folding_maps[0].append(F1)
    
while folded_graphs !=[]:
    duplicate_folded_graphs = folded_graphs
    folded_graphs = []
    for i in duplicate_folded_graphs:
        for c in i.cusps:
            F0 = i.fold(c,0)
            if is_in_list(F0, list_of_tracks)== False:
                list_of_tracks.append(F0)
                folded_graphs.append(F0)
            F1 = G.fold(c,1)
            if is_in_list(F1, list_of_tracks)== False:
                list_of_tracks.append(F1)
                folded_graphs.append(F1)


A = DiGraph(list_of_folding_maps)

print(A)
            


    
    











