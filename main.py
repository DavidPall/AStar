import sys


def solved(n):
    A = []
    count = 0
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(count)
            count += 1
        # print(A[i])
    return A


def printM(matrix):
    for row in matrix:
        print(row)


def up(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0] - 1][position[1]]
    matrix[position[0] - 1][position[1]] = 0
    return position[0] - 1, position[1]


def down(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0] + 1][position[1]]
    matrix[position[0] + 1][position[1]] = 0
    return position[0] + 1, position[1]


def right(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0]][position[1] + 1]
    matrix[position[0]][position[1] + 1] = 0
    return position[0], position[1] + 1


def left(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0]][position[1] - 1]
    matrix[position[0]][position[1] - 1] = 0
    return position[0], position[1] - 1


def find_pos(matrix, size, nr):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == nr:
                return row, col


def manhattan(matrix, size):
    solved_mx = solved(size)
    sum = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] != solved_mx[row][col]:
                pos = find_pos(matrix, size, solved_mx[row][col])
                sum += abs(pos[0] - row) + abs(pos[1] - col)
    return sum


input = False
solseq = False
pcost = False
nvisited = False
randf = False

for ind in range(len(sys.argv)):
    if sys.argv[ind] == "-input":
        input_file = sys.argv[ind+1]
        input = True

    if sys.argv[ind] == "-solseq":
        solseq = True

    if sys.argv[ind] == "-pcost":
        pcost = True

    if sys.argv[ind] == "-nvisited":
        nvisited = True

    if sys.argv[ind] == "-rand":
        randf = True
        N = sys.argv[ind+1]
        M = sys.argv[ind+2]

    if sys.argv[ind] == "-h":
        H = sys.argv[ind+1]

A = solved(3)
pos = (0, 0)

