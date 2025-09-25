
diction = {}


cycles = [[1, 12, 17, 13, 5], [1, 12, 17, 13, 8], [1, 12, 17, 15, 8], [1, 12, 5], [1, 12, 5, 13, 8], [1, 12, 7], [1, 12, 8], [1, 12, 8, 17, 13, 5], [1, 12, 8, 2, 17, 13, 5], [1, 12, 8, 19, 17, 13, 5], [1, 7], [1, 7, 12, 17, 13, 5], [1, 7, 12, 17, 13, 8], [1, 7, 12, 17, 15, 8], [1, 7, 12, 5], [1, 7, 12, 5, 13, 8], [1, 7, 12, 8], [1, 7, 12, 8, 17, 13, 5], [1, 7, 12, 8, 2, 17, 13, 5], [1, 7, 12, 8, 19, 17, 13, 5], [1, 8], [1, 8, 17, 12, 5], [1, 8, 17, 12, 7], [1, 8, 17, 13, 5], [1, 8, 2, 17, 12, 5], [1, 8, 2, 17, 12, 7], [1, 8, 2, 17, 13, 5], [1, 8, 19, 17, 12, 5], [1, 8, 19, 17, 12, 7], [1, 8, 19, 17, 13, 5], [2, 17, 12, 5, 13, 8], [2, 17, 12, 8], [2, 17, 13, 8], [2, 17, 15, 8], [5, 13], [5, 13, 8, 17, 12], [5, 13, 8, 19, 17, 12], [7, 12], [8, 17, 12], [8, 17, 13], [8, 17, 15], [8, 19, 17, 12], [8, 19, 17, 13], [8, 19, 17, 15], [17, 12], [17, 19], [17, 15, 19]]


for v in vertices:
    diction[v] = []
    for p in vertices:
        paths = G.all_simple_paths([v], [p])
        if (len(paths) != 0):
            for j in paths:
                for c in cycles:
                    if are_cyclically_equal(j,c) == False:
                        if p not in diction[v]:
                            diction[v].append(p)


    

def are_cyclically_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    if not list1:  # Both lists are empty
        return True
    
    n = len(list1)
    
    # Check all possible rotations
    for i in range(n):
        if list1 == list2[i:] + list2[:i]:
            return True
    
    return False



T= []
for c in cycles:
    for t in c:
        if t in T:
            continue
        else:
            T.append(t)

        



from itertools import permutations

for perm in permutations(cycles):
    perm_as_list = list(perm)