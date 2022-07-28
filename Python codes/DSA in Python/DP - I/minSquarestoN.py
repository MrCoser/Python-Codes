
# Online Python - IDE, Editor, Compiler, Interpreter

import math, sys
sys.setrecursionlimit(10**6)
def minStepsTo1(n,dp):
    #Implement Your Code Here
    
    # base case
    if n == 0:
        return 0
    
    ans = sys.maxsize
    root = int(math.sqrt(n))
    
    for i in range(1,root + 1):
        new = n-(i*i)
        if dp[new]== -1:
            small = minStepsTo1(n-(i*i),dp)
            dp[new] = small
            currans = 1 + small
            
        else:
            currans = 1 + dp[new]
        ans = min(ans, currans)
        
    return ans
        

    
n = int(input())
dp = [-1 for i in range(n+1)]
ans = minStepsTo1(n,dp)
print(ans)