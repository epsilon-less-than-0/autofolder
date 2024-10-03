def realedges(G, infpoly, labels = True): #input is graph and infinitesimal polygon info, returns list of real edges
    realedges = []
    marked = infpoly["marked"]
    unmarked = infpoly["unmarked"]
    allpolys = marked + unmarked
    if labels == True:
        # alledges = G.edges(sort=True)
        alledges = G.edges()
    else:
        # alledges = G.edges(sort=True, labels = False)
        alledges = G.edges(labels = False)

    for e in alledges:
        firstvertex = e[0]
        secondvertex = e[1]
        is_real_edge = True
        for j in allpolys:
            polygon = j[1]
            if firstvertex in polygon and secondvertex in polygon:
                is_real_edge = False
                break
        if is_real_edge:
            realedges.append(e)
    return sorted(realedges)

