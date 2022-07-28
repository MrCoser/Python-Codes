
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
    
    
    

def insertDuplicateNode(root):
    # Your code goes here

    if root is None:
        return None

    insertDuplicateNode(root.left)
    insertDuplicateNode(root.right)

    duplicateData = root.data
    duplicateNode = BinaryTreeNode(duplicateData)
    temp = root.left
    root.left = duplicateNode
    duplicateNode.left = temp


    return root
    
    
    
    
#main
root = takeTreeInput()
printTreeDetailed(root)
print()

insertDuplicateNode(root)
printTreeDetailed(root)