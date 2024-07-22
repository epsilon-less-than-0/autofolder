def realedges(G, infpoly): #input is graph and infinitesimal polygon info, returns list of real edges
    realedges = []
    marked = infpoly["marked"]
    unmarked = infpoly["unmarked"]
    allpolys = marked + unmarked
    alledges = G.edges(sort=True)
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
    return realedges
