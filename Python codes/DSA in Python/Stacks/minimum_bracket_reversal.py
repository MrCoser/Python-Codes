
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin
import math

# Returns count of minimum reversals for making
# expr balanced. Returns -1 if expr cannot be
# balanced.
def countBracketReversals(inputString) :
    # Your code goes here
    
    n = len(inputString)
    
    # Strings of odd lengths
    # can never be balanced
    if (n % 2 != 0):
        return -1
    
    left = 0
    right = 0
    
    for i in range(n):
        if (inputString[i] == "{"):
            left += 1
            
        else:
            if (left == 0):
                right += 1
                
            else:
                left -= 1
    
    return math.ceil(left / 2) + math.ceil(right / 2)
            




#main
print(countBracketReversals(stdin.readline().strip()))
