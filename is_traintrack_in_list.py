from traintrack import *
from cusp import *
from sage.graphs.views import EdgesView
from itertools import product
from sage.combinat.permutation import Permutations
import copy
from check_dict_values_cyclic import *
from transitionmatrix_folding import transitionmatrix_folding

def is_traintrack_in_list(train, ListOfTrains):
    for i in ListOfTrains:
        if i.is_isomorphic_to(train):
            print("Traintrack is in the list, at the %dth index" % ListOfTrains.index(i))
            return [True,ListOfTrains.index(i)]
    print("Traintrack is not in the list")
    return [False,None]