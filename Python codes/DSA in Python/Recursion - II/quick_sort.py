
# Online Python - IDE, Editor, Compiler, Interpreter

def partition(array, start, end):
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      
# The main function that implements QuickSort 
def quickSort(array, start, end):
      
    if (start < end):
          
        # p is partitioning index
        p = partition(array, start, end)
          
        # Sort elements before partition index
        # and after partition index
        quickSort(array, start, p - 1)
        quickSort(array, p + 1, end)
        
        
# main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, (n - 1))
print(*arr)