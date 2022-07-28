
# Online Python - IDE, Editor, Compiler, Interpreter

def isPrime(a):   ##function to check whether k is prime
    d = 2
    flag = False
    while d < a:
        if(a % d == 0):
            flag = True
            break
        d = d + 1
    return flag    
        
def PrintPrimesfrom2toN(N):  ##function that uses isPrime() to check if k (<= N) is prime or not, 
    k = 2                    ##and if it is, then print all the k's (from 2 to N)
    while k <= N:
        res = isPrime(k)
        if(not(res)):
            print(k, end=" ")
        k = k + 1 
        
N = int(input())
PrintPrimesfrom2toN(N)
            