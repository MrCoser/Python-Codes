
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    
    count = 0
    while(head is not None):
        count = count + 1
        head = head.next
        
    return count
    
def insertatI_iterative(head,i,data):
    if (i < 0) or(head is None):
        return head
        
    count = 0
    prev = None
    curr = head
    while (count < i):
        
        prev = curr
        curr = curr.next
        count += 1
    
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    
    return head
    
    




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
    i = int(stdin.readline().rstrip())
    printLinkedList(head)
    
    head = insertatI_iterative(head,i,2)
    printLinkedList(head)
    
    head = insertatI_iterative(head,5,3)
    printLinkedList(head)
    t -= 1