
# Online Python - IDE, Editor, Compiler, Interpreter

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
        
# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def constructBST(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not lst:
        return None
    
    # find middle
    mid = (len(lst) - 1) // 2
    
    # make the middle element the root
    root = BinaryTreeNode(lst[mid])
    
    # left subtree of root has all
    # values <arr[mid]
    root.left = constructBST(lst[:mid])
    
    # right subtree of root has all 
    # values >arr[mid]
    root.right = constructBST(lst[mid+1:])
    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root = constructBST(lst)
preOrder(root)