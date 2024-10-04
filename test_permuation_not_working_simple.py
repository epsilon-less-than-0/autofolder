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

G = Graph({0: [0, 1], 1: [0, 2], 2: [1, 3, 4], 3: [2, 3], 4:[2,4]})
G.allow_multiple_edges(True)
G.add_edges([(1,2,'s')])
infpoly = {'marked': [(1, [0]), (2, [1, 2]), (1, [3]), (1, [4])],'unmarked': []}
order = {0: [(0, 0), (0, 1)], 1: [(0, 1), (1, 2), (1,2,'s')], 2: [(1,2),(2,4),(2,3),(1,2,'s')], 3: [(3, 3), (2,3)], 4: [(4,4),(2,4)]}
side_swapping_edges = [(0, 0),(1, 2, 's'), (3, 3), (4, 4)]
singularity_type = {'marked': [1, 2, 1,1], 'unmarked': [], 'boundary': [1]}
c = cusp(2,((2,3),(2,4)))
cusps_list = [c]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping_edges)

T_LOR = T.deepcopy()
T_LOR.fold(T_LOR.cusps[0],1)
T_ROL = T.deepcopy()
T_ROL.fold(T_ROL.cusps[0],0)




