class cusp:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges
## vertex is in the form of a single int 
## edges in the form of a tuple of two tuples, each representing an edge as a tuple of two vertices
    def __str__(self):
        return f"cusp at vertex {self.vertex} with edges({self.edges})"
