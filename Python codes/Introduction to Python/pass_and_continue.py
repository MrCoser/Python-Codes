
# Online Python - IDE, Editor, Compiler, Interpreter

# code with continue statement
for i in range(1,31,1):
    if(i % 3 == 0):                ### gives numbers from  1 to 30, but simply skipping the cases 
        continue                   ### when i is divisible by 3
    print(i, end=" ")
print()    

# code with pass statement
for j in range(1,31,1):
    if(j % 3 == 0):                ### gives numbers from  1 to 30, but simply doing nothing in the cases 
        pass                       ### when i is divisible by 3
    print(j, end=" ")
print()    