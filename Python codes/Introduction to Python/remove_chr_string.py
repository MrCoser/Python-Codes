
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    temp = ""
    length = len(string)
    for i in range(length):
        if (string[i] != ch):
            temp = temp + string[i]
            
    return temp       
    
#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)