
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    #Your code goes here
    if (n == 0):
        return -1
    
    else:
        sum = 0
        for i in range(n):
            sum += arr[i]
            
        leftsum = 0
        for j in range(n):
            sum -= arr[j]
            if(sum == leftsum):
                return j
            leftsum += arr[j]
            
        
        return -1


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
    print(arrayEquilibriumIndex(arr, n))

    t-= 1