
# Online Python - IDE, Editor, Compiler, Interpreter

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        


# Given a binary search tree and a key, this function
# delete the key and returns the new root    

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
        
    
    def printTreeHelper(self, root):
        if root is None:
            return None
    
        print(root.data, end = ":")
        
        if root.left is not None:
            print("L:", end = "")
            print(root.left.data, end = ",")
        
        if root.right is not None:
            print("R:", end = "")
            print(root.right.data, end = "")
            
        print()    
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    
    def printTree(self):
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        self.printTreeHelper(self.root)
    
    
    def searchHelper(self, root, data):
        if root is None:
            return False
    
        if root.data == data:
            return True
    
        if root.data >= data:
            # call on left
            return self.searchHelper(root.left, data)
    
        else:
            # call on right
            return self.searchHelper(root.right, data)
    
    
    
    
    def search(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    
        return self.searchHelper(self.root, data)



    def insertHelper(self, root, data):
        if root is None:
            root = BinaryTreeNode(data)
            return root
    
    
        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
    
        else:
            root.right = self.insertHelper(root.right, data)
            return root
    
    
        
        
    def insert(self, data):
        
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    
        self.numNodes += 1     
        self.root = self.insertHelper(self.root, data)
        
        
    
    def min(self, root):
        if root is None:
            return 100000000   #some large positive number
        
        if root.left is None:
            return root.data
        
        
        return self.min(root.left)
    
    
    
    
    def deleteHelper(self, root, data):
        if root is None:
            return False, None
        
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        # case 1, when root is leaf
        if root.left is None and root.right is None:
            return True, None
        
        #case 2, when root has one child
        if root.left is None:
            return True, root.right
        
        if root.right is None:
            return True, root.left
        
        
        #case 3, when root has both children
        replace = self.min(root.right)
        root.data = replace
        deleted, newRightNode = self.deleteHelper(root.right, replace)
        root.right = newRightNode
        return True, root
    
    
    
      
    def delete(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        deleted, newRoot = self.deleteHelper(self.root, data)
        
        if deleted:
            self.numNodes -= 1
        
        self.root = newRoot
        return deleted
    
    
    def count(self):
        return self.numNodes
        
        
        
        
# main        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()