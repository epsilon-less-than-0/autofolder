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

G = Graph({0:[0,5],1:[1,8],2:[2,7],3:[3,6],4:[4,6],5:[0,6,8],6:[5,4,3,7],7:[8,6,2],8:[5,7,1]}) 
order = {0:[(0,5),(0,0)],1:[(1,8),(1,1)],2:[(2,7),(2,2)],3:[(3,6),(3,3)],4:[(4,6),(4,4)],5:[(0,5),(5,6),(5,8)],6:[(5,6),(4,6),(3,6),(6,7)],7:[(6,7),(2,7),(7,8)],8:[(5,8),(7,8),(1,8)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4])],"unmarked":[(4,[5,6,7,8])]}
singularity_type = {"marked":[1,1,1,1,1],"unmarked":[4],"boundary":[1]}
c = cusp(6,((3,6),(4,6)))
cusps_list = [c]
side_swapping = [(0,0),(1,1),(2,2),(3,3),(4,4)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)

G_copy = Graph({0:[0,5],1:[1,8],2:[2,7],3:[3,6],4:[4,6],5:[0,6,8],6:[5,4,3,7],7:[8,6,2],8:[5,7,1]}) 
order_copy = {0:[(0,5),(0,0)],1:[(1,8),(1,1)],2:[(2,7),(2,2)],3:[(3,6),(3,3)],4:[(4,6),(4,4)],5:[(0,5),(5,6),(5,8)],6:[(5,6),(4,6),(3,6),(6,7)],7:[(6,7),(2,7),(7,8)],8:[(5,8),(7,8),(1,8)]}
infpoly_copy = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4])],"unmarked":[(4,[5,6,7,8])]}
singularity_type_copy = {"marked":[1,1,1,1,1],"unmarked":[4],"boundary":[1]}
c_copy = cusp(6,((3,6),(4,6)))
cusps_copy = [c_copy]
side_swapping_copy = [(0,0),(1,1),(2,2),(3,3),(4,4)]
T_copy = StandardTrainTrack(G_copy,cusps_copy, order_copy,singularity_type_copy ,infpoly_copy,side_swapping_copy)