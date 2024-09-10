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

G = Graph({0:[0,5],1:[1,7],2:[2,7],3:[3,6],4:[4,6],5:[0,6,7],6:[5,4,3,7],7:[5,6,2,1]})
order = {0:[(0,0),(0,7)],1:[(1,1),(1,7)],2:[(2,2),(2,7)],3:[(3,3),(3,6)],4:[(4,4),(4,6)],5:[(0,5),(5,6),(5,7)],6:[(5,6),(4,6),(3,6),(6,7)],7:[(5,7),(6,7),(2,7),(1,7)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4])],"unmarked":[(3,[5,6,7])]}
singularity_type = {"marked":[1,1,1,1,1],"unmarked":[3],"boundary":[2]}
c1 = cusp(7,((1,7),(2,7)))
c2 = cusp(6,((3,6),(4,6)))
cusps_list = [c1,c2]
side_swapping = [(0,0),(1,1),(2,2),(3,3),(4,4)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)

G_copy = Graph({0:[0,5],1:[1,7],2:[2,7],3:[3,6],4:[4,6],5:[0,6,7],6:[5,4,3,7],7:[5,6,2,1]})
order_copy = {0:[(0,0),(0,7)],1:[(1,1),(1,7)],2:[(2,2),(2,7)],3:[(3,3),(3,6)],4:[(4,4),(4,6)],5:[(0,5),(5,6),(5,7)],6:[(5,6),(4,6),(3,6),(6,7)],7:[(5,7),(6,7),(2,7),(1,7)]}
infpoly_copy = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4])],"unmarked":[(3,[5,6,7])]}
singularity_type_copy = {"marked":[1,1,1,1,1],"unmarked":[3],"boundary":[2]}
c1_copy = cusp(7,((1,7),(2,7)))
c2_copy = cusp(6,((3,6),(4,6)))
cusps_list_copy = [c1_copy,c2_copy]
side_swapping_copy = [(0,0),(1,1),(2,2),(3,3),(4,4)]
T_copy = StandardTrainTrack(G_copy,cusps_list_copy, order_copy,singularity_type_copy ,infpoly_copy,side_swapping_copy)
