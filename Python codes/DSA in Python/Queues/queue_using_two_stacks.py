
# Online Python - IDE, Editor, Compiler, Interpreter

class QueueUsingTwoStacks:
    
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
        
    def enqueue(self, data):
        # TC :- O(N)
        while len(self.__stack1) != 0:
            self.__stack2.append(self.__stack1.pop())
        
        self.__stack1.append(data)
        
        while len(self.__stack2) != 0:
            self.__stack1.append(self.__stack2.pop())
        
        return
    
    def dequeue(self):
        # TC :- O(1)
        if len(self.__stack1) == 0:
            return -1
        return self.__stack1.pop()
        
    def front(self):
        if len(self.__stack1) == 0:
            return -1
        return self.__stack1[-1]
    
    def size(self):
        return len(self.__stack1)
    
    def isEmpty(self):
        return self.size() == 0
        
        
q = QueueUsingTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()