import sys
import random

# ----- FUNCTIONS -------

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


def inWrongPlace(matrix, size):
    counter = 0
    helper = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != helper:
                counter += 1
            helper += 1
    return counter


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


def randomizeMatrix(matrix, N, M, pos):
    myCounter = 0
    while M > 0:
        dir = random.randint(0, 4)
        if pos[0] != 0:
            if dir == 1:
                pos = up(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[1] != N - 1:
            if dir == 2:
                pos = right(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[0] != N - 1:
            if dir == 3:
                pos = down(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[1] != 0:
            if dir == 4:
                pos = left(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
    return matrix

# ------ CODE ------

input = False
solseq = False
pcost = False
nvisited = False
randf = False

for ind in range(len(sys.argv)):
    if sys.argv[ind] == "-input":
        input_file = sys.argv[ind + 1]
        input = True

    if sys.argv[ind] == "-solseq":
        solseq = True

    if sys.argv[ind] == "-pcost":
        pcost = True

    if sys.argv[ind] == "-nvisited":
        nvisited = True

    if sys.argv[ind] == "-rand":
        randf = True
        N = int(sys.argv[ind + 1])
        M = int(sys.argv[ind + 2])

    if sys.argv[ind] == "-h":
        H = int(sys.argv[ind + 1])


pos = (0, 0)

print()
if randf:
    A = randomizeMatrix(solved(N), N, M, pos)

printM(A)
