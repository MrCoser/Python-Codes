
# Online Python - IDE, Editor, Compiler, Interpreter
## Code for displaying pattern of the following type -
## 1 2 3 4
## 9 10 11 12         for N = 4
## 13 14 15 16
## 5 6 7 8

## or,
## 1 2 3 4 5
## 11 12 13 14 15
## 21 22 23 24 25     for N = 5 
## 16 17 18 19 20
## 6 7 8 9 10

N = int(input())
for i in range((N+1)//2):            ##for odd N
    for j in range(1, N+1):
        print(((N*2*i)+j), end=" ")
    print()
for i in range(N//2, 0, -1):         ##for even N
    for j in range(1, N+1):
        print(N*((2*i)-1)+j, end=" ")
    print()    