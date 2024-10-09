from traintrack import *
from cusp import *

def mirror(train):
    new_graph = train.graph.copy()
    new_order = reverse_dict_lists(train.vert_orders)
    new_infpoly = reverse_nested_lists(train.infpoly)
    new_cusp_list = []
    for c in train.cusps:
        vertex = c.vertex
        new_left = tuple(c.right)
        new_right = tuple(c.left)
        new_c = cusp(vertex, (new_left,new_right))
        new_cusp_list.append(new_c)
    new_side_swappers = train.side_swapping_edges[::-1]
    new_singularity_type = train.singularity_type.copy()

    T = StandardTrainTrack(new_graph, new_cusp_list, new_order, new_singularity_type, new_infpoly, new_side_swappers)
    return T







def reverse_dict_lists(d):
    return {key: list(reversed(value)) for key, value in d.items()}

def reverse_nested_lists(d):
    def reverse_inner_list(item):
        if isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], list):
            return (item[0], list(reversed(item[1])))
        return item

    return {key: [reverse_inner_list(item) for item in value] for key, value in d.items()}