
# Online Python - IDE, Editor, Compiler, Interpreter

def checkPalindrome(s):
    size = len(s)
    
    if (size == 0):
        return True
    
    if (size == 1):
        return True
    
    if (s[0] != s[size-1]):
        return False
    
    return checkPalindrome(s[1:(size-1):1])
    
# main
s = input()
bool_pal = checkPalindrome(s)
if (bool_pal):
    print("true")
else:
    print("false")