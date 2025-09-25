def find_other_integer(pair, v):
    if pair[0] == v:
        return pair[1]
    elif pair[1] == v:
        return pair[0]
    else:
        raise ValueError(f"{v} is not in the pair {pair}")