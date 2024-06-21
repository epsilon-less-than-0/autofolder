class cusp:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges
        self.left = edges[0]
        self.right = edges[1]
## vertex is in the form of a single int 
## edges in the form of a tuple of two tuples, each representing an edge as a tuple of two vertices, TUPLE MUST BE ORDERED. First left edge then right edge
    def __str__(self):
        return f"cusp at vertex {self.vertex} with edges({self.edges})"
    
    def left_vertex(self):
        if self.left[0] == self.vertex:
            return self.left[1]
        else:
            return self.left[0]
        
    def right_vertex(self):
        if self.right[0] == self.vertex:
            return self.right[1]
        else:
            return self.right[0]
