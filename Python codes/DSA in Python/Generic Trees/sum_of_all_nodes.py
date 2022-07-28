
# Online Python - IDE, Editor, Compiler, Interpreter

import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root
        
def sumOfAllNodes(root) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    #sum variable
    Sum = 0
    
    if root == None:
        return 0
    
    # Creating a queue and pushing the root
    q = []
    q.append(root)
  
    while len(q) != 0:
        n = len(q)
  
        # If this node has children
        while n > 0:
            # Dequeue an item from queue and
            # add it to variable "sum"
            p = q[0]
            q.pop(0)
            Sum += p.data
  
            # push all children of the dequeued item
            for i in range(len(p.children)):
                q.append(p.children[i])
            n-=1
    return Sum
    
#main
sys.setrecursionlimit(10**6)
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(sumOfAllNodes(root))