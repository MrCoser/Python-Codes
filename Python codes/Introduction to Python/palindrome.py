
# Online Python - IDE, Editor, Compiler, Interpreter

## program to check whether a number is palindrome or not
def checkPalindrome(num):
#Implement Your Code Here
    n = num
    flag = False
    rev = 0
    while (num != 0):
        r = num % 10
        rev = (rev*10) + r
        num = num // 10
        
    if(rev == n):
        flag = True
        
    return flag
    pass
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
