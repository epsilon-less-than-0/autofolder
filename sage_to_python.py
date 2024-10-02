from sage.all import Integer
from sage.structure.element import Matrix as SageMatrix


def sage_to_python(obj):
    if isinstance(obj, Integer):
        return int(obj)
    elif isinstance(obj, list):
        return [sage_to_python(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(sage_to_python(item) for item in obj)
    elif isinstance(obj, dict):
        return {sage_to_python(k): sage_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, SageMatrix):
        return {
            '__class__': 'Matrix',
            'rows': obj.nrows(),
            'cols': obj.ncols(),
            'data': [[int(x) for x in row] for row in obj]
        }
    return obj