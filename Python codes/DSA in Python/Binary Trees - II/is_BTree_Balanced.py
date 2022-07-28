
# Online Python - IDE, Editor, Compiler, Interpreter

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

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
    
    
def height(root):
    if root is None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))
    
    
def isBalanced(root):
    if root is None:
        return True
        
    lh = height(root.left)
    rh = height(root.right)
    
    if lh - rh > 1  or rh - lh > 1:
        return False
        
    if (isBalanced(root.left) == isBalanced(root.right)):
        return True
    else:
        return False
        
        
#main
btn = takeTreeInput()
printTreeDetailed(btn)
print(isBalanced(btn))
    