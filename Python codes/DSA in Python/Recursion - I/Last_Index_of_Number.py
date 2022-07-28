
# Online Python - IDE, Editor, Compiler, Interpreter

def lastIndex(arr, x):
    # Please add your code here
    size = len(arr)
    if (size == 0):
        return -1
        
    ans = lastIndex(arr[1:],x)
    if (ans != -1):
        return (ans + 1)
    else:
        if (x == arr[0]):
            return 0
        else:
            return -1
        

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x))