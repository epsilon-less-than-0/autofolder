from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from is_traintrack_in_list import *
from realedges import realedges


T_LOR_graph = Graph({0: [0, 1], 1: [0, 1, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 6], 7: [5, 7]})
T_LOR_graph.allow_multiple_edges(True)
# T_LOR_graph.add_edges([(2,3,'s'),(4,5,'s')])
T_LOR_graph.add_edges([(2,3),(4,5)])
T_LOR_infpoly = {'marked': [(1, [0]), (1, [1]), (2, [2, 3]), (2, [4, 5]), (1, [6]), (1, [7])],'unmarked': []}
T_LOR_order = {0: [(0, 0), (0, 1)], 1: [(0, 1), (1, 1), (1, 2)], 2: [(2, 3), (2, 3, 's'), (1, 2)], 3: [(2, 3), (3, 4), (2, 3, 's')], 4: [(3, 4), (4, 5), (4, 5, 's')],5: [(4, 5), (5, 7), (5, 6), (4, 5, 's')],6: [(6, 6), (5, 6)],7: [(7, 7), (5, 7)]}
T_LOR_side_swapping_edges = [(0, 0), (1, 1), (2, 3, 's'), (4, 5, 's'), (6, 6), (7, 7)]
T_LOR_singularity_type = {'marked': [1, 1, 1, 1, 2, 2], 'unmarked': [], 'boundary': [2]}
c0 = cusp(1,((0,1),(1,2)))
c1 = cusp(5,((5,6),(5,7)))
T_LOR_cusps_list = [c0,c1]
T_LOR = StandardTrainTrack(T_LOR_graph,T_LOR_cusps_list,T_LOR_order ,T_LOR_singularity_type,T_LOR_infpoly,T_LOR_side_swapping_edges)

one_graph = Graph({0: [0, 1, 2], 1: [0, 1],2: [0, 3],3: [2, 4],4: [3, 5],5: [4, 6, 7],6: [5, 6],7: [5, 7]})
one_graph.allow_multiple_edges(True)
# one_graph.add_edges([(2,3,'s'),(4,5,'s')])
one_graph.add_edges([(2,3),(4,5,)])
one_infpoly = {'marked': [(1, [0]), (1, [1]), (2, [2, 3]), (2, [4, 5]), (1, [6]), (1, [7])],'unmarked': []}
one_order = {0: [(0, 0), (0, 1), (0, 2)],1: [(1, 1), (0, 1)],2: [(0, 2), (2, 3), (2, 3, 's')],3: [(2, 3), (3, 4), (2, 3, 's')],4: [(3, 4), (4, 5), (4, 5, 's')],5: [(4, 5), (5, 7), (5, 6), (4, 5, 's')],6: [(6, 6), (5, 6)],7: [(7, 7), (5, 7)]}
one_side_swapping_edges = [(1, 1), (0, 0), (2, 3, 's'), (4, 5, 's'), (6, 6), (7, 7)]
one_singularity_type = {'marked': [1, 1, 1, 1, 2, 2], 'unmarked': [], 'boundary': [2]}
c0_one = cusp(0,((0,2),(0,1)))
c1_one = cusp(5,((5,6),(5,7)))
one_cusps_list = [c0_one,c1_one]
one = StandardTrainTrack(one_graph,one_cusps_list,one_order ,one_singularity_type,one_infpoly,one_side_swapping_edges)



