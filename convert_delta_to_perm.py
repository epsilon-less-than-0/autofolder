

def convert_delta_to_perm(delta):
    is_it_inverse = False
    if delta[5:10] == "^(-1)":
        is_it_inverse = True

    if is_it_inverse == False:
        ell = int(delta[7])
        em = int(delta[9])
        perm = Permutation(list(range(ell, em+1)))
        return perm
    else:
        j = int(delta[12])
        k = int(delta[14])
        permz = Permutation(list(reversed(range(j,k+1))))
        return permz

