from traintrack import *
from is_jointless import is_jointless

def jointless_tracks_in_automaton(AutomatonDict):
    tracks = [value for value in AutomatonDict.values()]
    jointless_tracks = []
    for T in tracks:
        if is_jointless(T)[0] == True:
            jointless_tracks.append(T)

    return jointless_tracks

        