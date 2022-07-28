
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input())
x = 1
n = (N+1)/2                        ##For N = 7, n = 4 and n1 = 3
n1 = (N-1)/2                       ## Similarly, for N = 5, n = 3 and n1 = 2

while x <= n:                      ##First loop starts....
    spaces = 1                     ##increasing spaces
    while spaces <= (x-1):
        print(" ", end="")
        spaces = spaces + 1
    j = 1
    while j <= x:                  ##increasing stars
        print("* ", end="")
        j = j + 1
    print()
    x = x + 1
y = n - n1
while y <= n1:                     ##Second loop starts....
    spaces = n1 - y                ##decreasing spaces
    while spaces >= 1:         
        print(" ", end="")
        spaces = spaces - 1
    k = 1                          ##decreasing stars
    while k <= (n1-y+1):
        print("* ",end="")
        k = k + 1
    print()
    y = y + 1