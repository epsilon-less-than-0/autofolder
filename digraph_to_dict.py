#converts a sagemath digraph to a dictionary
from json_encoder_and_decoder import *
from sage.matrix.constructor import matrix
from sage.all import Graph
from sage.all import DiGraph




def digraph_to_dict(G):
    return {
        'vertices': list(G.vertices()),
        'edges': encode_custom(G.edges()),
    }

def json_to_digraph(json_string):
    data = json.loads(json_string)
    G = DiGraph()
    G.allow_loops(True)
    G.add_vertices(data['vertices'])
    edges = decode_custom(data['edges'])
    G.add_edges(edges)
    for e in edges:
        current_label = G.edge_label(e[0],e[1])
        current_label['transition matrix'] = decode_custom( current_label['transition matrix'])
        G.set_edge_label(e[0],e[1],current_label)
    return G