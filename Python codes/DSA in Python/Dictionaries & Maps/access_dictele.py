
# Online Python - IDE, Editor, Compiler, Interpreter

a = {1:2, 3:4, "abc":{1,2,3}, 40:[3,4,5]}   # dictionary a
print(a)

print(a['abc'])
print(a.get(1))  # prints the value linked with the key

print(a.get(2))  # prints 'None'

print(a.keys())     # prints a list of keys
print(a.values())   # prints a list of values

for i in a:
    print(i, a[i])
    
    
for i in a.values():
    print(i)
    