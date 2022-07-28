
# Online Python - IDE, Editor, Compiler, Interpreter

# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def areSame (arr):       #function to check whether all elements in an array
    first = arr[0];      #are same, or not
     
    for i in range(1, len(arr)):
        if (arr[i] != first):
            return False;
           
    return True;
 
def secondLargestElement(arr, n):
    #Your code goes here
    
    MIN_VALUE = -2147483648
    
            
    
    if (n <= 1):
        return MIN_VALUE 
    elif (areSame(arr)):
        return MIN_VALUE
    else:
        for i in range(n):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j+1]):
                    (arr[j], arr[j+1]) = (arr[j+1], arr[j])    
                    
        
    return (arr[n-2])

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1