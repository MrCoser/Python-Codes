
# Online Python - IDE, Editor, Compiler, Interpreter

def sum_of_digits(n):
    if (n == 0):
        return 0
    
    return (n % 10 + sum_of_digits(n // 10))
    
# main
n = int(input())
res = sum_of_digits(n)
print(res)