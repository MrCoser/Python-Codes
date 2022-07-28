
# Online Python - IDE, Editor, Compiler, Interpreter

def string_to_integer(s):
    
    size = len(s)
    
    if (size == 0):
        return 
    
    if (size == 1):
        b = ord(s)
        return b - 48
    
    return int(s[size-1]) + (10*string_to_integer(s[0:(size-1):1]))
    
    
    
    
# main
s = input()
print(string_to_integer(s))