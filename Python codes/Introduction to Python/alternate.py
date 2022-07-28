
# Online Python - IDE, Editor, Compiler, Interpreter

N = int(input())
i = 1
while i <= N:
    if(i % 2 != 0):
        j = N-i+1
        while j >= 1:
            print("1", end="")
            j = j - 1
    else:
        k = N-i+1
        while k >= 1:
            print("0", end="")
            k = k - 1
    print()
    i = i + 1