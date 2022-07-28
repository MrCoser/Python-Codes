
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
    
def largestData(root):
    if root is None:
        return -1  #ideally should have been -inf
    
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    
    return max(leftLargest, rightLargest, root.data)
    
#main    
btn1 = takeTreeInput()
printTreeDetailed(btn1)
print(largestData(btn1))