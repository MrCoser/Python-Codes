
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d
# using gcd approach

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
    
    
def rotate(arr, n, d):
    #Your code goes here
    if (n == 0  and d == 0):
        return
    
    id = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
         
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
        

        
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1