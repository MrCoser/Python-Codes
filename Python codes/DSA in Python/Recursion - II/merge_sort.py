
# Online Python - IDE, Editor, Compiler, Interpreter

def merge(a1, a2, a):
    
    i = 0
    j = 0
    k = 0
    
    while i < len(a1) and j < len(a2):
        if (a1[i] < a2[j]):
            a[k] = a1[i]
            k = k + 1
            i = i + 1
            
        else:
            a[k] = a2[j]
            k = k + 1
            j = j + 1
            
                            
        while i < len(a1):        ## these two loops are here to ensure that,
            a[k] = a1[i]          ## the two sub-arrays a1 and a2 are completed 
            k = k + 1             ## till the very end
            i = i + 1
            
        while j < len(a2):
            a[k] = a2[j]
            k = k + 1
            j = j + 1
            
            
def mergeSort(arr, start, end):
    # Please add your code here
    
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = (start + end) // 2
    
    a1 = arr[start:mid]
    a2 = arr[mid:]
    mergeSort(a1, start, mid)
    mergeSort(a2, mid, end)
    
    merge(a1, a2, arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)