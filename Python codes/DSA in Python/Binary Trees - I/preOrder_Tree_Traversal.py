
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
	# Your code goes here
    if (root is None):
        return
    
    
    if (root):
        # First print the data of node
        print(root.data, end = " "),
 
        # Then recur on left child
        preOrder(root.left)
 
        # Finally recur on right child
        preOrder(root.right)



        
        
#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
preOrder(root)