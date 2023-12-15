def unique_in_order(sequence):
    matrix = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            matrix.append(sequence[i])
    return matrix
