from mirror import *
from traintrack import *

def filter_isomorphic_mirrors(track_list):
    track_list_update = track_list.copy()
    result = {}
    for track in track_list:
        if track not in track_list_update:
            continue
        else:
            mirrored = mirror(track)
            if track.is_isomorphic_to(mirrored) == True:
                result[track_list.index(track)] = track
                track_list_update.remove(track)
            else:
                track_list_update.remove(track)
                for huh in track_list_update:
                    if  mirrored.is_isomorphic_to(huh):
                        result[(track_list.index(track),track_list.index(huh))] = [track,huh]
                        track_list_update.remove(huh)
    return result

