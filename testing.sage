from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *


G = Graph({0:[0,1],1:[0,1,2],2:[1,2]})
order = {0:[(0,1),(0,0)],1:[(1,2),(1,1),(0,1)],2:[(2,2),(1,2)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2])],"unmarked":[]}
singularity_type = {"marked":[1,1,1],"unmarked":[],"boundary":[1]}
c = cusp(1,((1,2),(0,1)))
cusps = [c]


G_copy = Graph({0:[0,1],1:[0,1,2],2:[1,2]})
order_copy = {0:[(0,1),(0,0)],1:[(1,2),(1,1),(0,1)],2:[(2,2),(1,2)]}
infpoly_copy = {"marked":[(1,[0]),(1,[1]),(1,[2])],"unmarked":[]}
singularity_type_copy = {"marked":[1,1,1],"unmarked":[],"boundary":[1]}
c_copy = cusp(1,((1,2),(0,1)))
cusps_copy = [c_copy]

T = traintrack(G,cusps,order,singularity_type,infpoly)
T_copy = traintrack(G_copy,cusps_copy,order_copy,singularity_type_copy,infpoly_copy)

T_copy.fold(c_copy,1)

print(T.is_isomorphic_to(T_copy))

