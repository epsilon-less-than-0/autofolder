from traintrack import *

def is_jointless(track):
    marked_polygons = track.infpoly["marked"]
    monogons = []
    for marked in marked_polygons:
        if marked[0] == 1:
            monogons.append(marked[1])
    monogons = [item for sublist in monogons for item in sublist]
    if len(monogons) == 0:
        print("there are no marked monogons so train track is (vacuously) jointless")
        return True , []
    else:
        jointless_monogons = []
        for v in monogons:
            neighbors_of_v = track.graph.neighbors(v)
            for f in neighbors_of_v:
                if f == v:
                    neighbors_of_v.remove(f)
            if len(neighbors_of_v) == 1:
                jointless_monogons.append(v)
    
    if len(jointless_monogons) == 0:
        print("None of the marked monogons are jointless, so the traintrack is not jointless")
    elif len(jointless_monogons) < len(monogons):
        jointless_monogon_as_edges = []
        for j in jointless_monogons:
            edge = (j,j)
            jointless_monogon_as_edges.append(edge)
        print(f"Not all of the marked monogons are jointless, so the train track is not jointless. The jointless monogons are {jointless_monogon_as_edges}")
        return False , jointless_monogon_as_edges
    elif len(jointless_monogons) == len(monogons):
        jointless_monogon_as_edges = []
        for j in jointless_monogons:
            edge = (j,j)
            jointless_monogon_as_edges.append(edge)
        print("Every marked monogon is jointless, so the train track is jointles")
        return True , jointless_monogon_as_edges