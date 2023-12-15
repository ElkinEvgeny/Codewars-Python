def tower_builder(n_floors):
    matrix = []
    n = n_floors
    s = 0
    for i in range(1, n_floors+1):
        matrix.append((n-i) * ' '+(i+s)*'*'+' '*(n-i))
        s += 1
    return matrix
