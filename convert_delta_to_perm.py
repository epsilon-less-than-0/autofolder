from sage.combinat.permutation import Permutation
from sage.combinat.permutation import Permutations


def convert_delta_to_perm(delta, n):
    is_it_inverse = False
    if delta == None:
        return Permutations(n).identity()
    if delta[5:10] == "^(-1)":
        is_it_inverse = True
        

    if is_it_inverse == False:
        ell = int(delta[7])
        em = int(delta[9])
        perm = list(range(ell, em+1))
        perm.reverse()
        perm = list(Permutation(tuple(perm)))
        for i in range(1,n+1):
            if i not in perm:
                perm.insert(i-1,i)
        return Permutation(perm)
    else:
        j = int(delta[12])
        k = int(delta[14])
        permz = list((range(j,k+1)))
        permz.reverse()
        permz = list(Permutation(tuple(permz)))

        for i in range(1,n+1):
            if i not in permz:
                permz.insert(i-1,i)
        return Permutation(permz)

