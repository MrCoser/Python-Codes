
# Online Python - IDE, Editor, Compiler, Interpreter

# Print all words with frequency K
# We are given a string S, which consists of some words and a number K.
# The task is to print all words having frequency K

def wordsfreqK(s, K):
    
    words = s.split()
    
    d = {}   # empty dictionary
    
    for w in words:                                        # Alternative :
        if w in d:                                         # for w in words:
            d[w] = d[w] + 1                                #     d[w] = d.get(w,0) + 1
    
        else:
            d[w] = 1 
            
            
    for w in d:
        if d[w] == K:
            print(w)
            
    

s = input()
K = int(input())
wordsfreqK(s, K)