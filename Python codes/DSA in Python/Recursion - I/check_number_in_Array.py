
# Online Python - IDE, Editor, Compiler, Interpreter

''' My code


    def checkNumber(arr,x):
    # Please add your code here
    pass
    if (x == arr[0]):
        return True
    else:
        l = 1
        ans = checkNumber(arr[l:],x)
        return ans
        l = l + 1
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr,x):
    print('true')
else:
    print('false')'''

def checkNumber(arr,x):
    if len(arr)==0:
        return False
    
    if arr[0]==x:
        return True
    
    return checkNumber(arr[1:],x)



from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
