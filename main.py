import sys
import random
from dataclasses import dataclass

class Node:
    def __init__(self, matrix, size, pos, cost, cost_h, parent):
        self.matrix = matrix
        self.size = size
        self.pos = pos
        self.cost = cost
        self.cost_h = cost_h
        self.parent = parent

# ----- FUNCTIONS -------

# Letrehozza a megoldott kirakosnak megfelelo allapotot
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

# Kiirja a matrixot
def printM(matrix):
    print()
    for row in matrix:
        print(row)

#Felfele tolja az ures mezot
def up(matrix, position):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())
    new_matrix[position[0]][position[1]] = new_matrix[position[0] - 1][position[1]]
    new_matrix[position[0] - 1][position[1]] = 0
    return new_matrix,(position[0] - 1, position[1])

# Lefele tolja az ures mezot
def down(matrix, position):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())
    new_matrix[position[0]][position[1]] = new_matrix[position[0] + 1][position[1]]
    new_matrix[position[0] + 1][position[1]] = 0
    return new_matrix,(position[0] + 1, position[1])

# Jobbra tolja az ures mezot
def right(matrix, position):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())
    new_matrix[position[0]][position[1]] = new_matrix[position[0]][position[1] + 1]
    new_matrix[position[0]][position[1] + 1] = 0
    return new_matrix,(position[0], position[1] + 1)

# Balra tolja az ures mezot
def left(matrix, position):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())
    new_matrix[position[0]][position[1]] = new_matrix[position[0]][position[1] - 1]
    new_matrix[position[0]][position[1] - 1] = 0
    return new_matrix,(position[0], position[1] - 1)

# 1. Szamu heurisztika. Megszamlalja azon mezok szamat amelyek nincsenek jo helyen.
def inWrongPlace(matrix, size):
    counter = 0
    helper = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != helper:
                counter += 1
            helper += 1
    return counter

# Megtalalja az ures mezo poziciojat.
def find_pos(matrix, size, nr):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == nr:
                return row, col

# 2. Szamu heurisztika. Kiszamitja a mezok manhattan tavolsagat a helyuktol.
def manhattan(matrix, size):
    solved_mx = solved(size)
    sum = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] != solved_mx[row][col]:
                pos = find_pos(matrix, size, solved_mx[row][col])
                sum += abs(pos[0] - row) + abs(pos[1] - col)
    return sum


# File-bol beolvasott allapot
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

# Veletlen generalt allapot
def randomizeMatrix(matrix, N, M, pos):
    myCounter = 0
    while M > 0:
        dir = random.randint(0, 4)
        if pos[0] != 0:
            if dir == 1:
                (matrix,pos) = up(matrix, pos)
                M -= 1
        if pos[1] != N - 1:
            if dir == 2:
                (matrix,pos) = right(matrix, pos)
                M -= 1
        if pos[0] != N - 1:
            if dir == 3:
                (matrix,pos) = down(matrix, pos)
                M -= 1
        if pos[1] != 0:
            if dir == 4:
                (matrix,pos) = left(matrix, pos)
                M -= 1
    print("Random Matrix:")
    printM(matrix)
    return matrix

# Allapot osszehasonlitas
def compare(matrix1, size, matrix2):
    for row in range(size):
        for col in range(size):
            if matrix1[row][col] != matrix2[row][col]:
                return False
    return True

# Megoldasi szekvencia kiirasa
def printSolutionSequence(temp):
    if temp.parent != None:
        printSolutionSequence(temp.parent)
    printM(temp.matrix)


# Segedfuggveny, kiemeli a csomopontok heurisztikus arat
def takeCostH(e):
    return e.cost_h


# A*
def A_Star(matrix, size, pos, func, solseq, pcost, nvisited):
    Open = []
    Closed = []
    solved_mx = solved(size)
    nude = Node(matrix, size, pos, 0, func(matrix, size), None)
    visited = 1
    Open.append(nude)
    while len(Open) != 0:
        temp = Open[0]
        # printM(temp.matrix)
        if compare(temp.matrix,size,solved_mx):
            if solseq == True:
                printSolutionSequence(temp)
            if pcost == True:
                print("cost: {}".format(temp.cost))
            if nvisited == True:
                print("nodes visited: {}".format(visited))
            return True
        Closed.append(temp)
        Open.remove(temp)
        for dir in range(4):
            kid = None
            if dir == 0:
                if temp.pos[0] != 0:
                    temp_tupple = up(temp.matrix, temp.pos)
                    # print("up")
                    # printM(temp_tupple[0])
                    kid = Node(temp_tupple[0], size, temp_tupple[1], temp.cost + 1,
                                     temp.cost + 1 + func(temp_tupple[0], size), temp)
                else:
                    continue
            if dir == 1:
                if temp.pos[1] != size - 1:
                    temp_tupple = right(temp.matrix, temp.pos)
                    # print("right")
                    # printM(temp_tupple[0])
                    kid = Node(temp_tupple[0], size, temp_tupple[1], temp.cost + 1,
                               temp.cost + 1 + func(temp_tupple[0], size), temp)
                else:
                    continue
            if dir == 2:
                if temp.pos[0] != size - 1:
                    temp_tupple = down(temp.matrix, temp.pos)
                    # print("down")
                    # printM(temp_tupple[0])
                    kid = Node(temp_tupple[0], size, temp_tupple[1], temp.cost + 1,
                               temp.cost + 1 + func(temp_tupple[0], size), temp)
                else:
                    continue
            if dir == 3:
                if temp.pos[1] != 0:
                    temp_tupple = left(temp.matrix, temp.pos)
                    # print("left")
                    # printM(temp_tupple[0])
                    kid = Node(temp_tupple[0], size, temp_tupple[1], temp.cost + 1,
                               temp.cost + 1 + func(temp_tupple[0], size), temp)
                else:
                    continue
            visited += 1
            duplicant = False
            for nd in Open:
                if compare(nd.matrix, size, kid.matrix) :
                    if nd.cost > kid.cost:
                       Open.remove(nd)
                       # print("remove_open")
                    else:
                        duplicant = True
            for nd in Closed:
                if compare(nd.matrix, size, kid.matrix):
                    if nd.cost > kid.cost:
                        Closed.remove(nd)
                        # print("remove_closed")
                    else:
                        duplicant = True
            if duplicant == False:
                Open.append(kid)
                # print("append")
                Open.sort(key=takeCostH)
                # print("sort_open")



# ------ CODE ------

input = False
input_file = "default.txt"
solseq = False
pcost = False
nVisited = False
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
        nVisited = True

    if sys.argv[ind] == "-rand":
        randf = True
        N = int(sys.argv[ind + 1])
        M = int(sys.argv[ind + 2])

    if sys.argv[ind] == "-h":
        H = int(sys.argv[ind + 1])

if input:
    (matrix, size) = inputFileMatrix(input_file)
elif randf:
    matrix = randomizeMatrix(solved(N), N, M, (0,0))
    size = N
else:
    matrix = solved(3)
    size = 3



printM(matrix)
pos = find_pos(matrix,size, 0)


if H == 1:
    A_Star(matrix, size, pos, inWrongPlace, solseq, pcost, nVisited)
elif H == 2:
    A_Star(matrix, size, pos, manhattan, solseq, pcost, nVisited)
else:
    print("Wrong Function call. Try adding -h 1")




