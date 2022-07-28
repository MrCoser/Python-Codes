
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def pairSum0(l,n,sum = 0):
    # Write your code here
    
    m = [0] * 10**6
 
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
 
    twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
 
        twice_count += m[sum - arr[i]]
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
 
    # return the half of twice_count
    return int(twice_count / 2)



    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))