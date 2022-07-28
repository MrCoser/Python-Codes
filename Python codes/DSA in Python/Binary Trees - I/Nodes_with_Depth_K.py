
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
    
    
def printDepthK(root, k):
    if root is None:
        return
    
    if k == 0:
        print(root.data, end = " ")
        return
    
    printDepthK(root.left, (k-1))
    printDepthK(root.right, (k-1))
    
def printDepthK_Version2(root, k, d = 0):
    if root is None:
        return
    
    if k == d:
        print(root.data, end = " ")
        return
    
    printDepthK_Version2(root.left, k, d+1)
    printDepthK_Version2(root.right, k, d+1)
    
    
#main
root = takeTreeInput()
k = int(input())

printTreeDetailed(root)
printDepthK(root, k)
printDepthK_Version2(root, k)