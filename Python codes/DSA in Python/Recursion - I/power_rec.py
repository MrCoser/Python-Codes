
# Online Python - IDE, Editor, Compiler, Interpreter

def a_power_b(a,b):
    if (b == 0):
        return 1
    return a * a_power_b(a,(b-1))
    
    
    
    
a, b = input().split()
a = int(a)
b = int(b)
ans = a_power_b(a,b)
print(ans)