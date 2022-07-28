
# Online Python - IDE, Editor, Compiler, Interpreter

def binarySearch(a, x, si, ei):
    if (si > ei):
        return -1
        
    mid = (si + ei) // 2
    if (a[mid] == x):
        return mid
    
    elif (a[mid] > x):
        return binarySearch(a, x, si, mid - 1)
        
    else:
        return binarySearch(a, x, mid + 1, ei)
        
#main
a = [int(i) for i in input().split()]
si = int(input())
ei = int(input())
x = int(input())
print(binarySearch(a, x, si, ei))