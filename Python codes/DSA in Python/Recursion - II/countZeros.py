
# Online Python - IDE, Editor, Compiler, Interpreter

''' Naive approach
def count_zeros(n):
    if (n == 0):
        return 1
    
    cntzeros = 0
    
    while (n > 0):
        if (n % 10 == 0):
            cntzeros = cntzeros + 1
        n = n // 10
        
    return cntzeros '''

## Approach using recursion
def count_zeros(n):
    if (n < 0):
        n *= -1   #Make n positive
        
    if (n < 10):
        if (n == 0):
            return 1
        else:
            return 0
        
    smallAns = count_zeros(n // 10)
    if (n % 10 == 0):
        smallAns += 1
        
    return smallAns




# main
n = int(input())
print(count_zeros(n))