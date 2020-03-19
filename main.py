import sys

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

if input:
    print(input_file)