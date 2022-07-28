
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an integer n, using phone keypad find out and return
# all the possible strings that can be made using digits
# of input n.

def numalpha(key):
    
    li = {}  # empty hashmap
    
    li[0] = "";
    li[1] = "";
    li[2] = "abc";
    li[3] = "def";
    li[4] = "ghi";
    li[5] = "jkl";
    li[6] = "mno";
    li[7] = "pqrs";
    li[8] = "tuv";
    li[9] = "wxyz";
    
    return li[key]
    

    
def keypad(n):
    
    if n == 0:
        li = []
        li.append("")
        return li
    
    
    numal = numalpha(n % 10)
    small = keypad(n // 10)
    
    res = []
    
    for ele in small:
        for c in numal:
            
            res.append(ele + c)
    
    
    return res
    
    
    
n = int(input())
ans = keypad(n)
for ele in ans:
    print(ele)