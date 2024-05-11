from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *


G = Graph({0:[0,4],1:[1,6],2:[2,3,5],3:[2,3],4:[0,5,6],5:[4,6,2],6:[1,4,5]})
order = {0:[(0,4),(0,0)],1:[(1,6),(1,1),(0,1)],2:[(2,2),(2,5),(2,3)],3:[(3,3),(2,3)],4:[(0,4),(4,5),(4,6)],5:[(4,5),(2,5),(5,6)],6:[(4,6),(5,6),(1,6)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3])],"unmarked":[(3,[4,5,6])]}
singularity_type = {"marked":[1,1,1,1],"unmarked":[3],"boundary":[1]}
c = cusp(2,((2,3),(2,5)))
cusps = [c]


G_alt = Graph({0:[0,1],1:[0,1,4],2:[2,6],3:[3,5],4:[1,6,5],5:[4,6,3],6:[2,4,5]})
order_alt = {0:[(0,1),(0,0)],1:[(1,4),(1,1),(0,1)],2:[(2,2),(2,6)],3:[(3,3),(3,5)],4:[(1,4),(4,5),(4,6)],5:[(4,5),(3,5),(5,6)],6:[(4,6),(5,6),(2,6)]}
infpoly_alt = {"marked":[(1,[0]),(1,[1]),(1,[2]),(1,[3])],"unmarked":[(3,[4,5,6])]}
singularity_type_alt = {"marked":[1,1,1,1],"unmarked":[3],"boundary":[1]}
c_alt = cusp(1,((1,4),(0,1)))
cusps_alt = [c_alt]

T = traintrack(G,cusps,order,singularity_type,infpoly)
T_copy = traintrack(G_alt,cusps_alt,order_alt,singularity_type_alt,infpoly_alt)

# T_copy.fold(c_copy,1)

print(T.is_isomorphic_to(T_copy))