
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    
    l = 0
    r = 0
    length = len(string)
    for i in range(length):
        r += 1
        if (string[i] == " "):
            lst = list(string)
            (lst[l], lst[r]) = (lst[r], lst[l])
            l += 1
            r -= 1
  
        l = r + 1
        r = l
    
    
    return string
        

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)