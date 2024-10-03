    
from realedges import realedges

def give_label_after_folding(original_traintrack, folded_traintrack):
    differences = list_differences(list(original_traintrack.graph.edges(sort = True, labels=False)), list(folded_traintrack.graph.edges(sort = True, labels=False)))
    only_in_original = differences[0]
    only_in_folded = differences[1]
    folded_edges_real = realedges(folded_traintrack.graph,folded_traintrack.infpoly, labels = False)
    for e in folded_edges_real:
        #in the special case where the underlying graph has multiple edges (i.e. we have marked bigons) the edge_label output will be a list
        if e != only_in_folded[0]:
            new_label = original_traintrack.graph.edge_label(e[0],e[1])
            if type(new_label) == list:
                new_label = new_label[0]
            folded_traintrack.graph.set_edge_label(e[0],e[1],new_label)
        else:
            new_label = original_traintrack.graph.edge_label(only_in_original[0][0],only_in_original[0][1])
            if type(new_label) == list:
                new_label = new_label[0]
            folded_traintrack.graph.set_edge_label(e[0],e[1],new_label)




def list_differences(list_original, list_folded): #input two lists, two outputs: first output is list of things only in the first list, 
                                                #second output is list of things only in the second list
    set1 = set(list_original)
    set2 = set(list_folded)
    
    only_in_list_original = list(set1 - set2)
    only_in_list_folded = list(set2 - set1)
    
    return only_in_list_original, only_in_list_folded