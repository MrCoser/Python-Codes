
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def findUnique(arr, n) :
    #Yourcode goes here
    #using XOR approach
    n = len(arr)
    sum = 0
    for i in range(n):
        sum = sum^arr[i]
    return sum


#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1