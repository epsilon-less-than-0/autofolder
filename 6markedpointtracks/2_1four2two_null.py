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

G = Graph({0:[0,2],1:[1,2],2:[0,1,3],3:[2,4],4:[3,5],5:[4,7,6],6:[6,5],7:[7,5]})
order = {0:[(0,0),(0,6)],1:[(1,1),(1,6)],2:[(2,2),(2,8)],3:[(3,3),(3,11)],4:[(4,4),(4,10)],5:[(5,5),(5,10)],6:[(0,6),(6,7),(6,8),(1,6)],7:[(6,7),(7,9),(7,8)],8:[(6,8),(7,8),(2,8)],9:[(7,9),(9,10),(9,11)],10:[(9,10),(5,10),(4,10),(10,11)],11:[(9,11),(10,11),(3,11)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4]),(1,[5])],"unmarked":[(3,[6,7,8]),(3,[9,10,11])]}
singularity_type = {"marked":[1,1,1,1,1,1],"unmarked":[3,3],"boundary":[2]}
c0 = cusp(6,((0,6),(1,6)))
c1 = cusp(10,((4,10),(5,10)))
cusps_list = [c0,c1]
side_swapping = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)