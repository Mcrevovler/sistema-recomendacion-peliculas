def y(p, q):
    return p and q


def o(p, q):
    return p or q


def no(p):
    return not p


def implica(p, q):
    return (not p) or q


def bicond(p, q):
    return p == q