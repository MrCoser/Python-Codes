
# Online Python - IDE, Editor, Compiler, Interpreter

import sys
import queue



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
    
    
def height_of_tree(root):
    
    #edge case
    if root == None:
        return 0
    
    
    maximum = 0
    
    for child in root.children:
        maximum = max(height_of_tree(child), maximum)
        
    return (1 + maximum)








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





#main
sys.setrecursionlimit(10**6)

li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(height_of_tree(root))