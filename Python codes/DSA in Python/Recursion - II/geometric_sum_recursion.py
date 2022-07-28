
# Online Python - IDE, Editor, Compiler, Interpreter

def geometric_sum(k):
    if (k == 0):
        return 1
    
    return ((1/(2**k)) + geometric_sum(k-1))
            
#main
k = int(input())
res = geometric_sum(k)
print('%.5f' % res)