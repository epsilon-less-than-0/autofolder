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

G = Graph({0:[0,2],1:[1,2],2:[0,1,3],3:[2,4],4:[3,5],5:[4,7,6],6:[6,5],7:[7,5]})
G.allow_multiple_edges(True)
G.add_edges([(2,3,'s'),(4,5,'s')])
infpoly = {"marked":[(1,[0]),(1,[1]),(2,[2,3]),(2,[4,5]),(1,[6]),(1,[7])],"unmarked":[]}
order = {0:[(0,0),(0,2)],1:[(1,1),(1,2)],2:[(0,2),(2,3),(2,3,'s'),(1,2)],3:[(2,3),(3,4),(2,3,'s')],4:[(3,4),(4,5),(4,5,'s')],5:[(4,5),(5,7),(5,6),(4,5,'s')],6:[(6,6),(5,6)],7:[(7,7),(5,7)]}
singularity_type = {"marked":[1,1,2,2,1,1],"unmarked":[],"boundary":[2]}
c0 = cusp(2,((0,2),(1,2)))
c1 = cusp(5,((5,6),(5,7)))
cusps_list = [c0,c1]
side_swapping = [(0,0),(1,1),(2,3,'s'),(4,5,'s'),(6,6),(7,7)]
T = StandardTrainTrack(G,cusps_list,order,singularity_type,infpoly,side_swapping)