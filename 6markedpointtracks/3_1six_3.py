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

G = Graph({0:[0,6],1:[1,8],2:[2,8],3:[3,7],4:[4,7],5:[5,6],6:[0,5,7,8],7:[6,4,3,8],8:[1,6,7,2]})
order = {0:[(0,0),(0,6)],1:[(1,1),(1,8)],2:[(2,2),(2,8)],3:[(3,3),(3,7)],4:[(4,4),(4,7)],5:[(5,5),(5,6)],6:[(0,6),(5,6),(6,7),(6,8)],7:[(6,7),(4,7),(3,7),(7,8)],8:[(1,8),(6,8),(7,8),(2,8)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4]),(1,[5])],"unmarked":[(3,[6,7,8])]}
singularity_type = {"marked":[1,1,1,1,1,1],"unmarked":[3],"boundary":[3]}
c1 = cusp(6,((5,6),(0,6)))
c2 = cusp(7,((3,7),(4,7)))
c3 = cusp(8,((1,8),(2,8)))
cusps_list = [c1,c2,c3]
side_swapping = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)