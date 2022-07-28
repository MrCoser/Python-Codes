
# Online Python - IDE, Editor, Compiler, Interpreter

import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    
    l = len(lst)
    heap = []
    for i in range(k):
        heap.append(lst[i])
    
    # Loop for each element
    # and sort the array
    for i in range(k, l):
        heap.sort()
        
        if (heap[0] > lst[i]):
            continue
        
        else:
            heap.pop(0)
            heap.append(lst[i])
    
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')