# print cornered rectangle like this -
## ****
## *  *   for rows = 3 and columns = 4
## ****
print("This is Rectangle program")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(1,rows+1):
    for j in range(1,columns+1):
        if i==1 or i==rows or j==1 or j==columns:
            print("*",end='')
        else:
            print(" ",end='')
    print() 