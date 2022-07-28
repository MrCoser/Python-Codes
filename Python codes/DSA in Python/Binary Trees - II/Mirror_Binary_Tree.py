
# Online Python - IDE, Editor, Compiler, Interpreter


""" Change a tree so that the roles of the
    left and right pointers are swapped at
    every node.
 
So the tree...
        4
        / \
    2 5
    / \
    1 3
 
is changed to...
    4
    / \
    5 2
    / \
    3 1
"""


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
    
    

def mirrorBinaryTree(node):
 
    if (node == None):
        return
    else:
 
        temp = node
         
        """ do the subtrees """
        mirrorBinaryTree(node.left)
        mirrorBinaryTree(node.right)
 
        """ swap the pointers in this node """
        temp = node.left
        node.left = node.right
        node.right = temp

    
    
    

#if __name__ == '__main__':
    
root = takeTreeInput()
printTreeDetailed(root)
print()
mirrorBinaryTree(root)
printTreeDetailed(root)