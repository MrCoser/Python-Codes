
# Online Python - IDE, Editor, Compiler, Interpreter

def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    l = len(lst)
    
    for i in range(l):
        m = i*2
        ele = lst[i]
        
        if ((m+1) < l):
            if(ele < lst[m+1]):
                return False
        
        if ((m+2) < l):
            if ele < lst[m+2]:
                return False
    
   
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')