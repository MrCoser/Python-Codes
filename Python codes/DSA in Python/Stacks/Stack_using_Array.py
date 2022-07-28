
# Online Python - IDE, Editor, Compiler, Interpreter

class Stack :
    
    def __init__(self):
        self.__data = []
    
    def push(self, item):
        self.__data.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("Empty Stack !!!")
            return
        return self.__data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Empty Stack !!!")
            return
        return self.__data[len(self.__data) - 1]
    
    def size(self):
        return len(self.__data)
    
    def isEmpty(self):
        return self.size() == 0
        

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

while s.isEmpty():
    print(s.pop())
    