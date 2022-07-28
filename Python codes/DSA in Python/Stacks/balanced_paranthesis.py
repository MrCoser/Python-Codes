
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin

open = ["[", "{", "("]
close = ["]", "}", ")"]

def isBalanced(expression) :
	#Your code goes here
    str = []   #the stack
    for ele in expression:
        if ele in open:
            str.append(ele)
        
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not str:
                return False
            
            curr_char = str.pop()
            if curr_char == "(":
                if ele != ")":
                    return False
                
            if curr_char == "{":
                if ele != "}":
                    return False
            
            if curr_char == "[":
                if ele != "]":
                    return False
    
    if str:
        return False
    else:
        return True




#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")