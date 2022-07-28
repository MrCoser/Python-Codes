
# Online Python - IDE, Editor, Compiler, Interpreter

def firstIndex(arr, x):
    # Please add your code here
    pass
    if (len(arr) == 0):
        return -1
    if (x == arr[0]):
        return 0
    
    ans = firstIndex(arr[1:],x)
    if (ans == -1):
        return -1
    else:
        return (ans + 1)
        

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
