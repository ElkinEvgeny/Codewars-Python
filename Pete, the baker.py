def cakes(r, a):
    return min(map(lambda c: a.get(c, 0) // r[c], r))
