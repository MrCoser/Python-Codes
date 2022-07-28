
# Online Python - IDE, Editor, Compiler, Interpreter

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Length(root):
    if root is None:
        return 0
    
    return (1 + Length(root.left) + Length(root.right))
    

def takeTreeInput():
    
    rootData = int(input())
    if rootData == -1:
        return None
        
    root = BinaryTreeNode(rootData)
    leftTree = takeTreeInput()
    rightTree = takeTreeInput()
    
    root.left = leftTree
    root.right = rightTree
    
    return root
    
    

#main
root = takeTreeInput()
print(Length(root))