
# Online Python - IDE, Editor, Compiler, Interpreter

# Given a string (of length n), print all the subsequences
# of the given string.

# Subsequences contain all the strings of length varying
# from 0 to n. But the order of characters should remain
# same as in the input string.


def printSubsequences(string, empty):
    
    n = len(string)
    if n == 0:
        
        print(empty)
        return
            
    
    printSubsequences(string[1:], empty)
    printSubsequences(string[1:], (empty + string[0]))
    
    
    
    
    
    
    
string = input()
empty = ""
printSubsequences(string, empty)