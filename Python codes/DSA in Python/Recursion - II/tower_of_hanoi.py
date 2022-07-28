
# Online Python - IDE, Editor, Compiler, Interpreter

# Problem - Tower of Hanoi
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    pass
    if n == 0:
        return
    elif n == 1:
        print(source, dest)
        return
    else:
        # for n >= 2
        towerofhanoi(n-1, source, dest, aux)
        print(source, dest)
        towerofhanoi(n-1, aux, source, dest)
        


#Main
n=int(input())
towerofhanoi(n, 'a', 'b', 'c')