def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    stack, length = [[0, 0]], len(matrix)
    while len(stack):
        x, y = stack.pop()
        if matrix[x][y] == '.':
            matrix[x][y] = 'x'
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length:
                    stack.append((x, y))
    return matrix[length-1][length-1] == 'x'
