
# Online Python - IDE, Editor, Compiler, Interpreter

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elementsInRangeK1K2(root, k1, k2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    
    if root == None:
        return
 
    curr = root
    while curr:
        if curr.left == None:
             
            # check if current node lies
            # between n1 and n2
            if curr.data <= k2 and curr.data >= k1:
                print(curr.data, end = " ")
            curr = curr.right
            
        else:
            pre = curr.left
             
            # finding the inorder predecessor-
            # inorder predecessor is the right
            # most in left subtree or the left
            # child, i.e in BST it is the
            # maximum(right most) in left subtree.
            while (pre.right != None and
                   pre.right != curr):
                pre = pre.right
                         
            if pre.right == None:
                pre.right = curr;
                curr = curr.left
            else:
                pre.right = None
 
                # check if current node lies
                # between n1 and n2
                if curr.data <= k2 and curr.data >= k1:
                    print(curr.data, end = " ")
                curr = curr.right
        

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
k1, k2 = (int(i) for i in input().strip().split())
elementsInRangeK1K2(root, k1, k2)