
# Online Python - IDE, Editor, Compiler, Interpreter

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
btn1 = BinaryTreeNode(10)
btn2 = BinaryTreeNode(20)
btn3 = BinaryTreeNode(30)

btn1.left = btn2
btn1.right = btn3