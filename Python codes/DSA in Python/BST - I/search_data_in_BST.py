
# Online Python - IDE, Editor, Compiler, Interpreter

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Solution
def searchInBST(root, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    #Base case: root is null or key is present at root
    if root is None:
        return False
    
    if root.data == k:
        return True

    #Check if root value is less than k 
    if root.data < k:
        return searchInBST(root.right, k)
    
    #Else, root value is greater than k
    return searchInBST(root.left, k)





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
k=int(input())
ans = searchInBST(root, k)
if ans:
    print("true")
else:
    print("false")