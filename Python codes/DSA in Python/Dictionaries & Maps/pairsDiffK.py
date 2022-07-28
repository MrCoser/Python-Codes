
# Online Python - IDE, Editor, Compiler, Interpreter

def printPairDiffK(l, k):
    mydict=dict()
    count=0
    for currEle in l:
        pair1=currEle+k
        pair2=currEle-k
        if pair1 in mydict:
            count+=mydict[pair1]
        if k!=0 and pair2 in mydict:
            count+=mydict[pair2]
    
        mydict[currEle]=mydict.get(currEle,0)+1
           
    return count
   

    
# main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))