
# Online Python - IDE, Editor, Compiler, Interpreter

## check AB problem
## Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks 
## if the string was generated using the following rules:
## a. The string begins with an 'a'
## b. Each 'a' is followed by nothing or an 'a' or "bb"
## c. Each "bb" is followed by nothing or an 'a'
## If all the rules are followed by the given string, return true otherwise return false.
def checkAb(s):
    if len(s) == 0:
        return True
    if s[0] == 'a':	
        if len(s[1:]) == 0:
            return True
        else:
            if s[1] == 'a':
                return checkAb(s[1:])
            else:
                if s[2] == 'b':
                    return checkAb(s[3:])
                else:
                    return False
        
    else:
        return False


#main
s = input()
if checkAb(s):
    print('true')
else:
    print('false')