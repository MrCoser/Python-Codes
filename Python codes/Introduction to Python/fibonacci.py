
# Online Python - IDE, Editor, Compiler, Interpreter

## program to check whether a number is in Fibonacci sequence or not
def checkMember(n):
#Implement Your Code Here
    flag = False
    if (n==0 or n==1):
        flag = True
    else:
        a = 1
        b = 1
        c = 0
        cnt = 3
        while (cnt <= n):
            c = a + b
            a = b
            b = c
            if (c == n):
                flag = True
                break
            cnt += 1
        
              
    return flag
    pass

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")