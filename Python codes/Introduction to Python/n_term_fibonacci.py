
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input())
if (N==1 or N==2):  #for N=1 or N=2 
    print("1")

else:
    a = 1           #for N>=3
    b = 1
    c = 0
    i = 3
    while i <= N:
        c = a + b
        a = b
        b = c
        i = i + 1
    print(c)