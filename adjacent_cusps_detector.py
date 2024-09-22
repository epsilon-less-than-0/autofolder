def adjacent_cusps_detector(list_of_cusps):
    adjacent_cusps = []
    n = len(list_of_cusps)
    for i in range(n):
        for j in range(i + 1, n):
            is_adjacent, result = compare(list_of_cusps[i], list_of_cusps[j])
            if is_adjacent:
                adjacent_cusps.append(result)
    return adjacent_cusps


#this compares two cusps. The retured thing first gives you the left cusp then the right cusp, if they are adjacent
def compare(cusp1, cusp2): 
    cusp1_right_edge = cusp1.right
    cusp1_left_edge = cusp1.left
    cusp1_edges = [cusp1_left_edge,cusp1_right_edge]
    cusp2_right_edge = cusp2.right
    cusp2_left_edge = cusp2.left
    cusp2_edges = [cusp2_left_edge,cusp2_right_edge]
    for edge in cusp1_edges:
        if edge in cusp2_edges:
            if edge == cusp1_right_edge:
                return True , [(cusp1,cusp2),edge] #(left cusp, right cusp)
            else:
                return True , [(cusp2,cusp1),edge] #(left cusp, right cusp)
    return False , None
