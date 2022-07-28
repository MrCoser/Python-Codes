import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)

    return mat


def add_new_2(mat):
    
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c] != 0):

        r = random.randint(0,3)
        c = random.randint(0,3)

    mat[r][c] = 2


def current_state(mat):

    # Checking for number 2048 in mat
    for i in range(4):
        for j in range(4):

            if (mat[i][j] == 2048):
                return 'YOU WIN'
    
    # Checking for number 0 in mat
    for i in range(4):
        for j in range(4):

            if (mat[i][j] == 0):
                return 'GAME NOT OVER'
    
    # Checking for every row and column except for last row and last column
    for i in range(3):
        for j in range(3):

            if (mat[i][j] == mat[i+1][j]  or  mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'


    # Checking last row
    for j in range(3):
        if (mat[3][j] == mat[3][j+1]):
            return 'GAME NOT OVER'


    # Checking last column
    for i in range(3):
        if (mat[i][3] == mat[i+1][3]):
            return 'GAME NOT OVER'


    return 'YOU LOSE'





def compress(mat):
 
    # bool variable to determine
    # any change happened or not
    changed = False
 
    # empty mat
    new_mat = []
 
    # with all cells empty
    for i in range(4):
        new_mat.append([0] * 4)
         
    # here we will shift entries
    # of each cell to it's extreme
    # left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0
 
        # loop to traverse each column
        # in respective row
        for j in range(4):
            if(mat[i][j] != 0):
                 
                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]
                 
                if(j != pos):
                    changed = True
                pos += 1
 
    # returning new compressed matrix
    # and the flag variable.
    return new_mat, changed




def merge(mat):
     
    changed = False
     
    for i in range(4):
        for j in range(3):
 
            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
 
                # double current cell value and
                # empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
 
                # make bool variable True indicating
                # the new mat after merging is
                # different.
                changed = True
 
    return mat, changed
    


def reverse(mat):

    # empty mat
    new_mat = []

    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])


    return new_mat



def transpose(mat):

    # empty mat
    new_mat = []

    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])


    return new_mat        
    
def move_up(mat):
    #Implement This Function
    new_mat = transpose(mat)
 
    # then move left (calling all
    # included functions) then
    new_mat, changed = move_left(new_mat)
 
    # again take transpose will give
    # desired results
    new_mat = transpose(new_mat)
    return new_mat, changed

def move_down(mat):
    #Implement This Function
    new_mat = transpose(mat)
 
    # move right and then again
    new_mat, changed = move_right(new_mat)
 
    # take transpose will give desired
    # results.
    new_mat = transpose(new_mat)
    return new_mat, changed

def move_right(mat):
    #Implement This Function
    new_mat = reverse(mat)
 
    # then move left
    new_mat, changed = move_left(new_mat)
 
    # then again reverse matrix will
    # give us desired result
    new_mat = reverse(new_mat)
    return new_mat, changed

def move_left(mat):
    #Implement This Function
    new_mat, changed1 = compress(mat)
 
    # then merge the cells.
    new_mat, changed2 = merge(new_mat)
     
    changed = changed1 or changed2
 
    # again compress after merging.
    new_mat, temp = compress(new_mat)
 
    # return new matrix and bool changed
    # telling whether the mat is same
    # or different
    return new_mat, changed