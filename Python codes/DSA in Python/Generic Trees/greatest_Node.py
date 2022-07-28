
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
   
    
def maxDataNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    
    if tree==None:
        return None
    greatest=tree
    for i in tree.children:
        m=maxDataNode(i)
        if m.data>greatest.data:
            greatest=m
    
    return greatest

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
print(maxDataNode(tree).data)