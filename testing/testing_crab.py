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



G = Graph({0:[0,9],1:[1,8],2:[2,5],3:[3,4,7],4:[4,3],5:[2,6,7],6:[5,10,7],7:[5,6,3],8:[1,9,10],9:[8,0,10],10:[6,8,9]}) 
order = {0:[(0,0),(0,9)],1:[(1,1),(1,8)],2:[(2,2),(2,5)],3:[(3,4),(3,7),(3,3)],4:[(4,4),(3,4)],5:[(2,5),(5,6),(5,7)],6:[(5,6),(6,10),(6,7)],7:[(5,7),(6,7),(3,7)],8:[(1,8),(8,9),(8,10)],9:[(8,9),(0,9),(9,10)],10:[(6,10),(8,10),(9,10)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3]),(1,[4])],"unmarked":[(3,[5,6,7]),(3,[8,9,10])]}
singularity_type = {"marked":[1,1,1,1,1],"unmarked":[3,3],"boundary":[1]}
c = cusp(3,((3,7),(3,4)))
cusps_list = [c]
side_swapping = [(0,0),(1,1),(2,2),(3,3),(4,4)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)