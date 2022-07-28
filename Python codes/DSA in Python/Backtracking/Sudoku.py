
# Online Python - IDE, Editor, Compiler, Interpreter

# Function to Find the entry in
# the Grid that is still  not used
# Searches the grid to find an
# entry that is still unassigned. If
# found, the reference parameters
# row, col will be set the location
# that is unassigned, and true is
# returned. If no unassigned entries
# remains, false is returned.
# 'l' is a list  variable that has
# been passed from the solve_sudoku function
# to keep track of incrementation
# of Rows and Columns
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False


# Returns a boolean which indicates
# whether any assigned entry
# in the specified row matches
# the given number.
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 
# Returns a boolean which indicates
# whether any assigned entry
# in the specified column matches
# the given number.
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 
# Returns a boolean which indicates
# whether any assigned entry
# within the specified 3x3 box
# matches the given number
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
     
    # Check if 'num' is not already
    # placed in current row,
    # current column and current 3x3 box
    return (not used_in_row(arr, row, num) and
           not used_in_col(arr, col, num) and
           not used_in_box(arr, row - row % 3,
                           col - col % 3, num))

    
def solveSudoku(board):
    #Implement Your Code Here
    
    
    # 'l' is a list variable that keeps the
    # record of row and col in
    # find_empty_location Function   
    l =[0, 0]
     
    # If there is no unassigned
    # location, we are done   
    if(not find_empty_location(board, l)):
        return True
     
    # Assigning list values to row and col
    # that we got from the above Function
    row = l[0]
    col = l[1]
     
    # consider digits 1 to 9
    for num in range(1, 10):
         
        # if looks promising
        if(check_location_is_safe(board,
                          row, col, num)):
             
            # make tentative assignment
            board[row][col]= num
 
            # return, if success,
            # ya !
            if(solveSudoku(board)):
                return True
 
            # failure, unmake & try again
            board[row][col] = 0
             
    # this triggers backtracking       
    return False

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')