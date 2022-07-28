
# Online Python - IDE, Editor, Compiler, Interpreter

class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.children = list()



def printTreeRecDetailed(root):
    #edge case
    if root == None:
        return
    
    print(root.data, ":", end = "")
    for child in root.children:
        print(child.data, ",", end = "")
        
    print()    
    for child in root.children:
        printTreeRecDetailed(child)
        
        
        
        
def takeTreeInput():
    print("Enter root's data")
    rootData = int(input())
    if rootData == -1:
        return None
        
    
    root = TreeNode(rootData)
    
    print("Enter number of children for ", rootData)
    childrenCount = int(input())
    
    for j in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    
    return root 
    
    
    
    
    
# main
root = takeTreeInput()
printTreeRecDetailed(root)