
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def lcs(s, t) :
	#Your code goes here

    p = len(s)
    q = len(t)
    
    
    # declare an array 
    L = [[0]*(q+1) for i in range(p+1)]
    
    
    for j in range (p+1):
        for k in range(q+1):
            
            if (j == 0 or k == 0):
                L[j][k] = 0
                
            elif (s[j-1] == t[k-1]):
                L[j][k] = L[j-1][k-1] + 1
                
            else:
                L[j][k] = max(L[j-1][k] , L[j][k-1])
                
                
    return L[p][q] #since L[p][q] denotes the length of LCS
    
    
#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))