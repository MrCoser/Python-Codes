
# Online Python - IDE, Editor, Compiler, Interpreter

def subsetSum(l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    d = {}   # empty dictionary
    
    # initialise length (result)
    length = 0
    curr_sum = 0
    
    # Traverse throught the entire array
    for i in range(len(l)):
        
        curr_sum += l[i]
        if l[i] is 0 and length is 0:
            length = 1
            
        if curr_sum is 0:
            length = i+1
            
        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Looks if current sum is seen
        # before
        if curr_sum in d:
            length = max(length, i - d[curr_sum] )
        else:
 
            # else put this sum in dictionary
            d[curr_sum] = i
 
    return length


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))