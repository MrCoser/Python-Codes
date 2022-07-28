
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


        
        
# Recursive function to print all the nodes at distance k
# int the tree(or subtree) rooted with given root. See
def printkDistanceNodeDown(root, k):
     
    # Base Case
    if root is None or k < 0 :
        return
     
    # If we reach a k distant node, print it
    if k == 0 :
        print(root.data)
        return
     
    # Recur for left and right subtree
    printkDistanceNodeDown(root.left, k-1)
    printkDistanceNodeDown(root.right, k-1)        
        
        
        
def nodesAtDistanceK(root, node, k) :
	#Your code goes here


    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1
 
    # If target is same as root. Use the downward function
    # to print all nodes at distance k in subtree rooted with
    # target or root
    if root.data == node:
        printkDistanceNodeDown(root, k)
        return 0
     
    # Recur for left subtree
    dl = nodesAtDistanceK(root.left, node, k)
     
    # Check if target node was found in left subtree
    if dl != -1:
         
        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dl + 1 == k :
            print(root.data)
     
        # Else go to right subtreee and print all k-dl-2
        # distant nodes
        # Note: that the right child is 2 edges away from
        # left chlid
        else:
            printkDistanceNodeDown(root.right, k-dl-2)
 
        # Add 1 to the distance and return value for
        # for parent calls
        return 1 + dl
 
    # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
    # Note that we reach here only when node was not found
    # in left subtree
    dr = nodesAtDistanceK(root.right, node, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data)
        else:
            printkDistanceNodeDown(root.left, k - dr - 2)
        return 1 + dr
 
    # If target was neither present in left nor in right subtree
    return -1








	


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

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])
nodesAtDistanceK(root, target, k)