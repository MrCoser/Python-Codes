
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin
from queue import Queue

class Stack:
    def __init__(self):
        self.__q1 = Queue()
        self.__q2 = Queue()
        self.__count = 0

    def getSize(self):
        return self.__q1.qsize()

    def empty(self):
        return self.getSize() == 0

    def push(self, data):
        self.__q1.put(data)
        self.__count += 1

    def pop(self):
        if self.__q1.empty() is True:
            return -1
            
        while self.getSize()>1:
            self.__q2.put(self.__q1.get())
            
        res = self.__q1.get()
        self.__count -= 1
        
        #swapping the two queues by their names
        temp = self.__q1
        self.__q1 = self.__q2
        self.__q2 = temp
        
        return res

    def top(self):
        if self.__q1.empty() is True:
            return -1
            
        while self.getSize()>1:
            self.__q2.put(self.__q1.get())
            
        res = self.__q1.get()
        self.__q2.put(res)
        
        #swapping the two queues by their names
        temp = self.__q1
        self.__q1 = self.__q2
        self.__q2 = temp
        
        return res


#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 :
		print(stack.getSize())

	else :
		if stack.empty() :
			print("true")
		else :
			print("false")

	q -= 1