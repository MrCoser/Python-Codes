
# Online Python - IDE, Editor, Compiler, Interpreter


import sys

def intersections(arr1, n, arr2, m):
    #Your code goes here
    for i in range(0,n):
        for j in range(0,m):
            if (arr1[i] == arr2[j]):
                print(arr2[j], end=" ")
                arr2[j] = sys.maxsize
                break
'''
lets say arr1 = 2 3 4 2


and arr2 = 2 0 0 0


so what is array Intersection here?


2


yes


now lets remove line 10 form our code 


arr2[j] = -999999


remove this line and if we dry run now


first 2 of arr1 will find 2 of arr2 and print 2


now last 2 of arr1 will find first 2 of arr2 and print again 2


so total two 2s are printed


and we dont want that right


so when first time we print 2


we chagne the value or arr2[j]


now arr1 = 2 3 4 2


but arr2 = -99999 0 0 0 


so now 2nd 2 of arr1 wont find any 2 and it will print 2 only once


that is what we want

so when the element of the second array is already processed you change it to -99999
so that it is not encountered the second time in the upper loop

'''

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1
