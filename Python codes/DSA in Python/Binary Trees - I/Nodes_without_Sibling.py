
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



def printNodesWithoutSibling(root) :
	# Your code goes here

    
    # Base Case
    if root is None:
        return
 
    # If this is an internal node , recur for left
    # and right subtrees
    if root.left is not None and root.right is not None:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)
 
    # If left child is NULL, and right is not, print
    # right child and recur for right child
    elif root.right is not None:
        print(root.right.data, end = " ")
        printNodesWithoutSibling(root.right)
 
    # If right child is NULL and left is not, print
    # left child and recur for left child
    elif root.left is not None:
        print(root.left.data, end = " ")
        printNodesWithoutSibling(root.left)











#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

	

# Main
root = takeInput()
printNodesWithoutSibling(root)