def smaller(arr):
    matrix = []
    for i in range(len(arr)):
        sum = 0
        for n in range(i+1, len(arr)):
            if arr[i] > arr[n]:
                sum += 1
        matrix.append(sum)
    return matrix
