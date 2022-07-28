
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
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
    
    
    
    

    

def isBST_Alt(root):
    if root == None:
        return 1000000, -1000000, True
        
    leftMin, leftMax, isLeftBST = isBST_Alt(root.left)
    rightMin, rightMax, isRightBST = isBST_Alt(root.right)
    
    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    
    isBST = True
    if root.data <= leftMax or root.data > rightMin:
        isBST = False
        
    if not(isLeftBST) or not(isRightBST):
        isBST = False
        
    return minimum, maximum, isBST
    
    
    
    


#if __name__ == '__main__':
root = takeTreeInput()
printTreeDetailed(root)
print(isBST_Alt(root))