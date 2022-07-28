
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def insertionSort(arr, n) :  
    #Your code goes here
    for step in range( 1 , len(arr)):
        key = arr[step]
        j = step - 1
        
# Compare key with each element on the left of it until an element smaller
# than it is found
        # For descending order, change key<array[j] to key>array[j].
        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1

        # Place the key at after the element just smaller than it.
        arr[j + 1 ] = key 

#taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n)

    t-= 1