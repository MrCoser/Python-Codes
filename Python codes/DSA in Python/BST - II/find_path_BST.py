
# Online Python - IDE, Editor, Compiler, Interpreter

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
# Returns true if there is a path from
# root to the given node. It also
# populates 'arr' with the given path
def hasPath(root, arr, x):
     
    # if root is None there is no path
    if (not root):
        return False
     
    # push the node's value in 'arr'
    arr.append(root.data)    
     
    # if it is the required node
    # return true
    if (root.data == x):    
        return True
     
    # else check whether the required node
    # lies in the left subtree or right
    # subtree of the current node
    if (hasPath(root.left, arr, x) or
        hasPath(root.right, arr, x)):
        return True
     
    # required node does not lie either in
    # the left or right subtree of the current
    # node. Thus, remove current node's value 
    # from 'arr'and then return false    
    arr.pop(-1)
    return False        
        
        
        
def findPathBST(root,data):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return None
    
    arr = []
    
    
    if(hasPath(root, arr, data)):
        arr.reverse()
        return arr
    
    else:
        return []
        
    
    

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
data = int(input())
path = findPathBST(root,data)
if path is not None:
    for ele in path:
        print(ele,end=' ')