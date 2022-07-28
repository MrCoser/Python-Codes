
# Online Python - IDE, Editor, Compiler, Interpreter

##implement a function to check whether a number is armstrong number or not
## Print output as specified in the question.
def checkArmstrong(n):
    digits = 0
    res = 0
    r = 0
    flag = False
    num = n
    n1 = num
    
    ##first, we find the number of digits in the number n
    while (n != 0):
        n = n // 10          
        digits += 1
                
    ##then, we will create a variable res (= r**digits), which will be used for
    ##comparison with n to check if it is armstrong number or not
    while (n1 != 0):
        r = n1 % 10
        res += (r**digits)
        n1 = n1 // 10
        
    if(res == num):
        flag = True
        
    return flag
pass

n = int(input())
armstrong = checkArmstrong(n)
if(armstrong):
    print("true")
else:
    print("false")