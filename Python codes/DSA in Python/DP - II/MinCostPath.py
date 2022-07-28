
# Online Python - IDE, Editor, Compiler, Interpreter


import sys
from sys import stdin

def minCostPath(input, mRows, nCols) :
	#Your code goes here

    if (nCols < 0 or mRows < 0):
        return sys.maxsize
    elif (mRows == 1 and nCols == 1):
        return input[0][0]
    else:
        return input[mRows-1][nCols-1] + min(minCostPath(input, mRows-1, nCols-1), minCostPath(input, mRows-1, nCols), minCostPath(input, mRows, nCols-1) )
 
#A utility function that returns minimum of 3 integers */
def min(x, y, z):
    if (x < y):
        return x if (x < z) else z
    else:
        return y if (y < z) else z





# taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))