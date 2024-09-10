from realedges import realedges
from sage.matrix.constructor import matrix
from give_label_after_folding import give_label_after_folding


#this gives edge labeling to a traintrack that comes from a folding, and also KNOWN THAT IT IS NOT ISOMORPHIC TO THE ORIGINAL ONE
#it also returns the corresponding transition matrix
#the folded traintrack has no edgelabel , this will give it

def give_edge_label_non_isomorphic_after_folding(original_traintrack, folded_traintrack, fold_here_cusp, direction):

    give_label_after_folding(original_traintrack,folded_traintrack)
        
    ListofRealEdges_original = realedges(original_traintrack.graph,original_traintrack.infpoly)
    ListofRealEdges_folded = realedges(folded_traintrack.graph, folded_traintrack.infpoly)

    transitionmatrix_list_of_rows = create_zero_matrix(len(ListofRealEdges_folded))

    column_counter = 0
    for row in transitionmatrix_list_of_rows:
        row[column_counter] = 1
        column_counter = column_counter + 1

    if direction == 0:
        star_column = int(original_traintrack.graph.edge_label(fold_here_cusp.right[0],fold_here_cusp.right[1]))
        star_row = int(original_traintrack.graph.edge_label(fold_here_cusp.left[0],fold_here_cusp.left[1]))
        transitionmatrix_list_of_rows[star_row - 1][star_column - 1] = transitionmatrix_list_of_rows[star_row - 1][star_column - 1]+1
    else:
        star_column = int(original_traintrack.graph.edge_label(fold_here_cusp.left[0],fold_here_cusp.left[1]))
        star_row = int(original_traintrack.graph.edge_label(fold_here_cusp.right[0],fold_here_cusp.right[1]))
        transitionmatrix_list_of_rows[star_row - 1][star_column - 1] = transitionmatrix_list_of_rows[star_row - 1][star_column - 1]+1

    M = matrix(transitionmatrix_list_of_rows)
    return M

def list_differences(list_original, list_folded):
    set1 = set(list_original)
    set2 = set(list_folded)
    
    only_in_list_original = list(set1 - set2)
    only_in_list_folded = list(set2 - set1)
    
    return only_in_list_original, only_in_list_folded

def create_zero_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]