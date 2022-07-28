
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an integer n, using phone keypad find out and print
# all the possible strings that can be made using digits 
# of input n.


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