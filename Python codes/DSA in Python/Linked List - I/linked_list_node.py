
# Online Python - IDE, Editor, Compiler, Interpreter
# Linked List Node
class Node :
    
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(13)
b = Node(15)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)