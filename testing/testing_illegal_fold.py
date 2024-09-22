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



G = Graph({0:[0,1],1:[0,2,1],2:[1,3,2],3:[3,2]}) 
order = {0:[(0,0),(0,1)],1:[(0,1),(1,2),(1,1)],2:[(1,2),(2,3),(2,2)],3:[(2,3),(3,3)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3])],"unmarked":[]}
singularity_type = {"marked":[1,1,1,1],"unmarked":[],"boundary":[2]}
c_1 = cusp(1,((1,2),(0,1)))
c_2 = cusp(2,((2,3),(1,2)))
cusps_list = [c_1,c_2]
side_swapping = [(0,0),(1,1),(2,2),(3,3)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)


G_copy = 
order_copy = =
infpoly_copy = =
singularity_type_copy = =
c_copy = =
cusps_copy = =
side_swapping_copy = =



T_copy = StandardTrainTrack(G_copy,cusps_copy, order_copy,singularity_type_copy ,infpoly_copy,side_swapping_copy)