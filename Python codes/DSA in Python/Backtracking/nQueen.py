
# Online Python - IDE, Editor, Compiler, Interpreter

def isSafe(row,cols,board,n):
    i=row-1
    while i>=0:
        if board[i][cols]==1:
            return False
        i-=1
    i=row-1
    j=cols-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i=row-1
    j=cols+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
        
    return True
    
    
    pass



def nQueenHelper(row,board,n):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
                
        print()
        return
    for cols in range(n):
        if isSafe(row,cols,board,n) is True:
            board[row][cols]=1
            nQueenHelper(row+1,board,n)
            board[row][cols]=0
            
            
            
    
            
    pass

    
def nQueen(n):
    #Implement Your Code Here
    if n==0:
        return
    if n==1:
        print(1)
        return
    board=[[0 for j in range(n)] for i in range(n)]
    nQueenHelper(0,board,n)
    pass


n = int(input())
nQueen(n)