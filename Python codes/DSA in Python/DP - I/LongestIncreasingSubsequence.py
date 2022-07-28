
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def lis(arr): 
    # Write your code here
    
    n = len(arr)
    # Creating the sorted list
    b = sorted(list(set(arr)))
    m = len(b)
 
    # Creating dp table for storing the answers of sub problems
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
 
    # Finding Longest common Subsequence of the two arrays
    for i in range(n+1):
 
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif arr[i-1] == b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]   # dp[-1][-1] will contain length of LIS

        

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))