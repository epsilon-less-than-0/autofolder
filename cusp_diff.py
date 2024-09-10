
#returns a cusp that is in train2 but not in train 1, assuming they only differ by one cusp

def cusp_diff(train1, train2):
    vertices_1 = []
    vertices_2 = []

    for cusp in train1.cusps:
        vertices_1.append(cusp.vertex)

    for cusp in train2.cusps:
        vertices_2.append(cusp.vertex)

    new_vertex_in_2 = list_differences(vertices_1,vertices_2)[1]

    for c in train2.cusps:
        if c.vertex == new_vertex_in_2[0]:
            return c
    



def list_differences(list_original, list_folded): #input two lists, two outputs: first output is list of things only in the first list, 
                                                #second output is list of things only in the second list
    set1 = set(list_original)
    set2 = set(list_folded)
    
    only_in_list_original = list(set1 - set2)
    only_in_list_folded = list(set2 - set1)
    
    return only_in_list_original, only_in_list_folded
