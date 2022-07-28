
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin
def maxfreq(arr):
    #Write your code here 
    d = {}   #create an empty dictionary
    
    count = 0
    item = ''
    
    
    for ele in reversed(arr):
        d[ele] = d.get(ele, 0) + 1
        
        if d[ele] >= count:
            count, item = d[ele], ele
            
            
    return(item)
        
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))