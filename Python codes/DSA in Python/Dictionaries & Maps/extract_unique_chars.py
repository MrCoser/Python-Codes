
# Online Python - IDE, Editor, Compiler, Interpreter

def uniqueChar(s): 
    # Write your code here
    
    res = ""
    d = {}
    for i in range(len(s)):
        
        if(s[i]) in d:
            pass
            
        else:
            res += s[i]
            d[s[i]] = True
            
            
    return res


# Main 
s=input() 
print(uniqueChar(s))