from sage.graphs.views import EdgesView
import cusp
class traintrack:
    def __init__(self, graph, cusps, infpoly):
        self.graph = graph
        self.cusps = cusps
        self.infpoly = infpoly
    ## graph as a Sagemath graph
    ## cusps as a list of objects of class cusp

    def in_poly(self,vertex):
        v = vertex
        for i in self.infpoly:
            for j in i:
                if j == v:
                    return True
                else 

    def fold(self,cusp,direction):
        G = self.graph
        cusp_vertex = cusp.vertex
        left_vertex = cusp.left_vertex()
        right_vertex = cusp.right_vertex()
        vertices = G.vertices(sort = True)
        star_vertex = len(vertices)
        G.add_vertices([star_vertex])
        G.add_edges([(star_vertex, left_vertex), (star_vertex,right_vertex), (star_vertex, cusp_vertex)])
        G.delete_edges([(cusp_vertex,left_vertex),(cusp_vertex,right_vertex)])
        if direction == 0: ## right over left
            G.contract_edge(star_vertex,left_vertex)
        else:
            G.contract_edge(star_vertex,right_vertex)

        new_cusps = 

        return traintrack(G,)

