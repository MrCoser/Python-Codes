
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

def printLevelWise(root):
    # Your code goes here

    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while (not (q.empty())):
        currentNode = q.get()
        print(str(currentNode.data), end=":")
        if currentNode.left != None:
            q.put(currentNode.left)
            print('L:' + str(currentNode.left.data), end=",")
        else:
            print('L:' + "-1", end=",")

        if currentNode.right != None:
            q.put(currentNode.right)
            print('R:' + str(currentNode.right.data), end="")
        else:
            print('R:' + "-1", end="")

        print()


#Taking level-order input using fast I/O method
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


# Main
root = takeTreeInput()
printLevelWise(root)