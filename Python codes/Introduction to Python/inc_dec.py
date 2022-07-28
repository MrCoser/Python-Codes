
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input())
i = 1
while i <= N:       
    spaces = N - i                ## print spaces 
    while spaces >= 1:
        print(" ",end="")
        spaces = spaces - 1
    j = i                         ##now print increasing numbers    
    while j <= ((2*i)-1):
        print(j,end="")
        j = j + 1
    k = ((2*i)-2)                 ##now print decreasing numbers    
    while k >= i:
        print(k,end="")
        k = k - 1
    print()                       ##program ends.....
    i = i + 1