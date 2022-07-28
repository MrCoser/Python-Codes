
# Online Python - IDE, Editor, Compiler, Interpreter

##implement a function to print values of temperatures in fahrenheit and celsius
def printTable(start,end,step):
    i = start
    while i <= end:
        c = ((i-32)*5) / 9
        print(i, end=" ")
        print(int(c))
        i = i + step
pass        
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)