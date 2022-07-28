
# Online Python - IDE, Editor, Compiler, Interpreter

class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.children = list()




        
n1 = TreeNode(5)
n2 = TreeNode(7)
n3 = TreeNode(8)
n4 = TreeNode(9)
n5 = TreeNode(11)
n6 = TreeNode(2)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)

n2.children.append(n5)
n3.children.append(n6)
