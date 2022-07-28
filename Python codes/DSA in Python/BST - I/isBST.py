
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
    
    
    
    
def minTree(root):
    if root == None:
        return 1000000  # a large positive number
        
    return min(minTree(root.left), minTree(root.right), root.data)
    
    
def maxTree(root):
    if root == None:
        return -1000000  # a large negative number
        
    return max(maxTree(root.left), maxTree(root.right), root.data)




    
def isBST(root):
    if root == None:
        return True
        
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    
    if root.data > rightMin  or  root.data <= leftMax:
        return False
        
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    
    return isLeftBST and isRightBST
    




#if __name__ == '__main__':
root = takeTreeInput()
printTreeDetailed(root)
print(isBST(root))