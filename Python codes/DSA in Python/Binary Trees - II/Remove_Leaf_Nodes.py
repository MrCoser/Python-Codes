
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
    
    

def removeLeaves(root):
    if root is None:
        return None
        
    if root.left is None and root.right is None:
        return None
        
    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    
    return root
    
    
    

#if __name__ == '__main__':
    
root = takeTreeInput()
printTreeDetailed(root)
print()
root = removeLeaves(root)
printTreeDetailed(root)