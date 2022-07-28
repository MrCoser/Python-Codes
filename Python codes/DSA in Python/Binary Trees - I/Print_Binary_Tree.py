
# Online Python - IDE, Editor, Compiler, Interpreter

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def printTree(root):
    
    if root is None:
        return 
    
    print(root.data)
    printTree(root.left)
    printTree(root.right)
    

def printTreeDetailed(root):
    
    if root is None:
        return 
    
    print(root.data, end = ":")
    
    if root.left is not None:
        print("L", root.left.data, end = ",")
        
    if root.right is not None:
        print("R", root.right.data)
    print()
    
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)    
    
    
#main    
btn1 = BinaryTreeNode(10)
btn2 = BinaryTreeNode(20)
btn3 = BinaryTreeNode(30)
btn4 = BinaryTreeNode(40)
btn5 = BinaryTreeNode(50)

btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5


printTreeDetailed(btn1)