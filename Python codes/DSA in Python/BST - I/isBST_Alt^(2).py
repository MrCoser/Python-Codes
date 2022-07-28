
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
    
    
    
    

    

def isBST_Alt2(root, min_Range, max_Range):
    if root == None:
        return True
    
    if root.data < min_Range  or  root.data > max_Range:
        return False
    
    return (isBST_Alt2(root.left, min_Range, root.data - 1) and isBST_Alt2(root.right, root.data, max_Range))
    
    


#if __name__ == '__main__':
root = takeTreeInput()
min_Range = int(input())
max_Range = int(input())

printTreeDetailed(root)
print(isBST_Alt2(root, min_Range, max_Range))