import sys

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


def inputFileMatrix(input_file):
    fin = open(input_file, "r")
    size = int(fin.readline())
    matrix = []
    for i in range(size):
        line = fin.readline()
        line = line.split(" ")
        matrix.append([])
        for word in line:
            matrix[i].append(int(word))
    return matrix, size

# def stdInputMatrix():
#     print("Enter Dö size of matrix:")
#     size = input("Size:")
#     matrix = []
#     for i in range(size):
#         print("Enter a line of the matrix:")
#         line = input()
#         line = line.split(" ")
#         matrix.append([])
#         for word in line:
#             matrix[i].append(int(word))
#     return matrix, size


# ------ CODE ------

input = False
input_file = "default.txt"
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

if input:
    (matrix, size) = inputFileMatrix(input_file)
    printM(matrix)


