
# Online Python - IDE, Editor, Compiler, Interpreter

# fibonacci using DP

# Normal approach (using recursion) :-
# def fibb(n):
#    if ((n == 1) or (n == 0)):
#      return n
#    
#    ans1 = fibb(n-1)
#    ans2 = fibb(n-2)
#
#    ans = ans1 + ans2  
#    return ans


def fibbDP(n,dp):
    if ((n == 0) or (n == 1)):
        return n
    
    # if-else block for (n-1)    
    if dp[n-1] == -1:
        ans1 = fibbDP(n-1,dp)
        dp[n-1] = ans1 
    else:
        ans1 = dp[n-1]
        
    
    # if-else block for (n-2)
    if dp[n-2] == -1:
        ans2 = fibbDP(n-2,dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]
        
        
    Ans = ans1 + ans2
    return Ans
    
    
    
n = int(input())
dp = [-1 for i in range(n+1)]
ans = fibbDP(n,dp)
return ans