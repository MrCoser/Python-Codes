
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin


def findDuplicate(arr, n) :
    #Your code goes here
    sum = 0
    for i in range(n):
        sum += arr[i]
        
    return sum - (((n - 1)* (n - 2)) // 2)


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1