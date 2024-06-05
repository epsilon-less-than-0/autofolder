from traintrack import *
from sage.combinat.permutation import Permutations
import copy

from sage.graphs.views import EdgesView
from cusp import cusp
from itertools import product

from check_dict_values_cyclic import *

class marked_traintrack:
    def __init__(self, traintrack, vertical_intersection_info):
        self.topological_traintrack = traintrack
        self.vertical_intersection_info = vertical_intersection_info



    def is_it_standard(self):
        for value in self.vertical_intersection_info.values():
            if not isinstance(value, list) or len(value) != 1:
                return False
        return True
    
    