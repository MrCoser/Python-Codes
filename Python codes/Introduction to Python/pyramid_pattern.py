
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input())
i = 1
while i <= N:                    ##First half of pattern
    spaces = 1
    while spaces <= (i-1):
        print(" ", end="")
        spaces = spaces + 1
    j = i
    while j <= N:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1
k = 1
while k <= (N-1):               ##Second half of pattern
    spaces = N - k - 1
    while spaces >= 1:
        print(" ", end="")
        spaces = spaces - 1
    l = N - k 
    while l <= N:
        print(l, end="")
        l = l + 1
    print()
    k = k + 1