
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
    
    

# Function to find height of a tree
def height(root, ans):
    if (root == None):
        return 0
 
    left_height = height(root.left, ans)
 
    right_height = height(root.right, ans)
 
    # update the answer, because diameter
    # of a tree is nothing but maximum
    # value of (left_height + right_height + 1)
    # for each node
    ans[0] = max(ans[0], 1 + left_height +
                             right_height)
 
    return 1 + max(left_height,
                   right_height)



# Function to find diameter of binary tree
def diameterOfBinaryTree(root) :
    # Your code goes here

    if root is None:
        return 0
    
    ans = [-999999999999] # This will store
                          # the final answer
    height_of_tree = height(root, ans)
    return ans[0]

    
    
    

#if __name__ == '__main__':
    
root = takeTreeInput()

printTreeDetailed(root)
print()
diameterOfBinaryTree(root)
printTreeDetailed(root)