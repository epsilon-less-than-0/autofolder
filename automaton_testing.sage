from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *

from traintrack import *
from cusp import *
from sage.graphs.views import EdgesView
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from is_traintrack_in_list import *
from standardizing import *


G = Graph({0:[0,1],1:[0,1,2],2:[1,2]})
order = {0:[(0,1),(0,0)],1:[(1,2),(1,1),(0,1)],2:[(2,2),(1,2)]}
infpoly = {"marked":[(1,[0]),(1,[1]),(1,[2])],"unmarked":[]}
singularity_type = {"marked":[1,1,1],"unmarked":[],"boundary":[1]}
