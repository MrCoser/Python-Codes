
# Online Python - IDE, Editor, Compiler, Interpreter

import heapq
def kSmallest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    
    l = len(lst)
    heap = []
    for i in range(k):
        heap.append(lst[i])
    
    heapq._heapify_max(heap)
    # Loop for each element
    # and sort the array
    for i in range(k, l):
        
        if (heap[0] > lst[i]):
            heapq._heapreplace_max(heap, lst[i])
        
        else:
            continue
    
    return heap


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')