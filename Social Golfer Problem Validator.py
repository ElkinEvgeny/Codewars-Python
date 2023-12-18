from itertools import permutations
from collections import Counter
def valid(a):
    str_ = "".join([''.join(i) for i in sum([],a)])
    p = Counter(str_)

    if len(set(p.values())) > 1:
        return False
    
    strong = []
    for i in a:
        for m in i:
            matrix = list(permutations(list(m), 2))
            for g in matrix:
                strong.append(g)
    con = Counter(strong)
    if len(set(con.values())) > 1:
            return False
    else:
        return True
