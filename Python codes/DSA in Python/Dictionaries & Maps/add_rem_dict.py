
# Online Python - IDE, Editor, Compiler, Interpreter

a = {1:2, 3:4, "abc":{1,2,3}, 40:[3,4,5]}   # dictionary a
print(a)

a['tuple'] = {1,2,3,4}
a[1] = 10     # previous value of 2
              # will be replaced with 10
print(a)


b = {3:4, 'the':6, 2:100}
a.update(b)   # updates the keys and values of a as per b
              # keys which are in common, will be updated with the new values of b
print(a)


a.pop(40)       # argument is the key to be deleted from a
del a[3]        # deletes the value specified as a[(key)]
print(a)


a.clear()       # clears the dictionary a
print(a)

del a           # deletes the dictionary a
