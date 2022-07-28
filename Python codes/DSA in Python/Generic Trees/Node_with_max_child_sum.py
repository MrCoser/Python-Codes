
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

    
def maxSumHelper(tree, resNode, maxSum):
    
    #Base / Edge case
    if tree == None:
        return
    
    #currsum - contains the sum of root 
    #and it's children
    currSum = tree.data
    cnt = len(tree.children)
    
    
    for i in range(cnt):
        currSum += tree.children[i].data
        resNode, maxSum = maxSumHelper(tree.children[i],
                                     resNode, maxSum)
 
    # if curr is greater than sum,
    # update it
    if currSum > maxSum:
 
        # resultant node
        resNode = tree
        maxSum = currSum
     
    return resNode, maxSum
    
    

def maxSumNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
     
    # resultant node with max
    # sum of children and node
    resNode, maxSum = treeNode(None), 0
    resNode, maxsum = maxSumHelper(tree, resNode,
                                       maxSum)
 
    # return the key of resultant node
    return resNode, maxSum


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
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)