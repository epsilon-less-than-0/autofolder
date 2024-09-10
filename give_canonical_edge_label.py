from realedges import realedges

def give_canonical_edge_label(track):
    ListofRealEdges = realedges(track.graph,track.infpoly)

    RealEdgeLabel = 1
    for e in ListofRealEdges:
        track.graph.set_edge_label(e[0], e[1], str(RealEdgeLabel))
        RealEdgeLabel = RealEdgeLabel + 1

