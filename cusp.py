from sage_to_python import sage_to_python

class cusp:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.edges = edges
        self.left = tuple(sorted(list(edges[0]))) #LEFT EDGE at zero position
        self.right = tuple(sorted(list(edges[1]))) #RIGHT EDGE at one position
## vertex is in the form of a single int 
## edges in the form of a tuple of two tuples, each representing an edge as a tuple of two vertices, TUPLE MUST BE ORDERED. First left edge then right edge
## LEFT EDGE FIRST THEN RIGHT EDGE
    def __str__(self):
        return f"cusp at vertex {self.vertex} with left edge{self.left} and right edge{self.right}"
    
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
        
    def to_json(self):
        return {
            '__class__': 'cusp',
            'vertex': sage_to_python(self.vertex),
            'edges': [
                sage_to_python(list(self.left)),
                sage_to_python(list(self.right))
            ]
        }

    @classmethod
    def from_json(cls, data):
        if isinstance(data, dict):
            vertex = data['vertex']
            edges = (tuple(data['edges'][0]), tuple(data['edges'][1]))
            return cls(vertex, edges)
        elif isinstance(data, cusp):
            return data
        else:
            raise ValueError(f"Unexpected data type for cusp.from_json: {type(data)}")

    def __repr__(self):
        return f"cusp(vertex={self.vertex}, edges=({self.left}, {self.right}))"
