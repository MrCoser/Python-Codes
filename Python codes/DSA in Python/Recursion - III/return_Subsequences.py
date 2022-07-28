
# Online Python - IDE, Editor, Compiler, Interpreter

# Given a string (of length n), return
# all the subsequences of the given string.

def subsequences(string):
    #Implement Your Code Here
    
    n = len(string)
    
    # base case
    if n == 0:
        li = []
        li.append("")
        return li
    
    
    smallerOutput = subsequences(string[1:])
    output = []
    
    for ele in smallerOutput:
        output.append(ele)
        
    for ele in smallerOutput:
        output.append(string[0] + ele)
        
        
    return output


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)