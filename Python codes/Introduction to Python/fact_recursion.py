
# Online Python - IDE, Editor, Compiler, Interpreter

# Factorial program using recursion in Python

def fact(n):
  if (n == 0):
      return 1
  return n * fact(n-1)
  
n = int(input())
res = fact(n)  
print(res)