import sys
import random
from dataclasses import dataclass

class Node:
    matrix: []
    size: int
    pos: (int, int)
    cost: int
    cost_h: int
    parent: Node

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
    return matrix,(position[0] - 1, position[1])


def down(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0] + 1][position[1]]
    matrix[position[0] + 1][position[1]] = 0
    return matrix,(position[0] + 1, position[1])


def right(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0]][position[1] + 1]
    matrix[position[0]][position[1] + 1] = 0
    return matrix,(position[0], position[1] + 1)


def left(matrix, position):
    matrix[position[0]][position[1]] = matrix[position[0]][position[1] - 1]
    matrix[position[0]][position[1] - 1] = 0
    return matrix,(position[0], position[1] - 1)


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


def randomizeMatrix(matrix, N, M, pos):
    myCounter = 0
    while M > 0:
        dir = random.randint(0, 4)
        if pos[0] != 0:
            if dir == 1:
                (matrix,pos) = up(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[1] != N - 1:
            if dir == 2:
                (matrix,pos) = right(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[0] != N - 1:
            if dir == 3:
                (matrix,pos) = down(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
        if pos[1] != 0:
            if dir == 4:
                (matrix,pos) = left(matrix, pos)
                M -= 1
                print("Direction: {}".format(dir))
                myCounter += 1
                print("Step: {}".format(myCounter))
                printM(matrix)
    return matrix

def is_solved(matrix, size, solved_mx):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] != solved_mx[row][col]:
                return False
    return True


def printSolutionSequence(temp):
    if temp.parent != None:
        printSolutionSequence(temp.parent)
    printM(temp.matrix)

def A_Star(matrix, size, pos, func, solseq, pcost, nvisited):
    Open = []
    Closed = []
    solved_mx = solved(size)
    nude = Node(matrix, size, pos, 0, func(matrix, size), None)
    visited = 1
    Open.append(nude)
    while len(Open) != 0:
        temp = Open[0]
        if is_solved(temp.matrix,size,solved_mx):
            if solseq == True:
                printSolutionSequence(temp)
            if pcost == True:
                print("cost: {}".format(temp.cost))
            if nvisited == True:
                print("nodes visited: {}".format(visited))
            return True
        for dir in range(4):
            if dir == 0:
                if pos[0] != 0:
                    temp_tupple = up(temp.matrix, temp.pos)
                    Open.append(Node(temp_tupple[0], size, temp_tupple[1], temp.cost + 1, temp.cost + 1 + manhattan(temp_tupple[0], size), temp))
            if dir == 1:
                if pos[1] != N - 1:
                    temp_tupple = right(temp.matrix, temp.pos)
            if dir == 2:
                if pos[0] != N - 1:
                    temp_tupple = down(temp.matrix, temp.pos)
            if dir == 3:
                if pos[1] != 0:
                    temp_tupple = left(temp.matrix, temp.pos)


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


elif randf:
    matrix = randomizeMatrix(solved(N), N, M, (0,0))
    size = N
else:
    matrix = solved(3)
    size = 3


printM(matrix)
pos = find_pos(matrix,size, 0)


