
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


# helper function         
def helper(head, n, pos):
    if (head is None):
        return -1
    
    if (head.data == n):
        return pos
    
    ans = helper(head.next, n, pos + 1)
    return ans


# Function to find node of a linked list with integer data 'N' 
def findNode(head, n) :
    # Write your code here.
    return helper(head, n, 0)



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = findNode(head, n)
    printLinkedList(head)

    t -= 1 