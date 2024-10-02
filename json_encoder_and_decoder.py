from sage_to_python import sage_to_python
from traintrack import *
from sage.matrix.constructor import matrix


def encode_custom(obj):
    if hasattr(obj, 'to_json'):
        return encode_custom(obj.to_json())
    obj = sage_to_python(obj)
    if isinstance(obj, dict):
        return {str(k): encode_custom(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return type(obj)(encode_custom(v) for v in obj)
    elif isinstance(obj,EdgesView):
        return [encode_custom(edge) for edge in obj]
    return obj

def decode_custom(dct):
    if isinstance(dct, dict) and '__class__' in dct:
        class_name = dct['__class__']
        if class_name == 'StandardTrainTrack':
            return StandardTrainTrack.from_json(dct)
        elif class_name == 'traintrack':
            return traintrack.from_json(dct)
        elif class_name == 'cusp':
            return cusp.from_json(dct)
        elif class_name == 'Matrix':
            return matrix(dct['data'])
    return dct