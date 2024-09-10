from realedges import realedges
ListofRealEdges = realedges(T.graph,T.infpoly)

RealEdgeLabel = 1
for e in ListofRealEdges:
    T.graph.set_edge_label(e[0], e[1], str(RealEdgeLabel))
    RealEdgeLabel = RealEdgeLabel + 1