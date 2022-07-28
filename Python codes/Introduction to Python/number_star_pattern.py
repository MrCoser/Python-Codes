
# Online Python - IDE, Editor, Compiler, Interpreter
## program to print the following pattern --
## 5432*
## 543*1
## 54*21                       for N = 5
## 5*321
## *4321

n = int(input())
i = 1
cntx = 1     ##impose the condition 1 <= cntx < cnty <= n
cnty = 1
while (i <= n):
    j = n
    while (j >= 1):
        if((cntx + cnty) != (n + 1)):
            print(j, end="")
        else:
            print("*", end="")
        
        cnty = cnty + 1
        if (cnty == (n+1)):
            cnty = 1
            break
        j = j - 1    
    print()
    cntx = cntx + 1
    i = i + 1