
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import setrecursionlimit
setrecursionlimit(10**8)


def multiply(m,n):
    if (m == 0 or n == 0):
        return 0
    
    return (m + multiply(m, n-1))
    
    
# main
m = int(input())
n = int(input())
res = multiply(m,n)
print(res)