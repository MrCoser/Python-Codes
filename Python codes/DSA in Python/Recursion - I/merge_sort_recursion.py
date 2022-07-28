
# Online Python - IDE, Editor, Compiler, Interpreter

def merge(arr1,size1,arr2,size2,arr):
    i=0
    j=0
    k=0
    while i<size1 and j<size2 :
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            k+=1
            i+=1
        else:
            arr[k]=arr2[j]
            k+=1
            j+=1
    while i<size1:
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<size2:
        arr[k]=arr2[j]
        k+=1
        j+=1
    
    
    pass

def mergeSort(arr,size):
    if size==0 or size==1:
        return
    arr1=[]
    arr2=[]
    size1=size//2
    size2=size-size1
    for i in range(size1):
        arr1.append(arr[i])
    for i in range(size1,size,1):
        arr2.append(arr[i])
    mergeSort(arr1,size1)
    mergeSort(arr2,size2)
    merge(arr1,size1,arr2,size2,arr)
        
    
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr,n)
print(*arr)
