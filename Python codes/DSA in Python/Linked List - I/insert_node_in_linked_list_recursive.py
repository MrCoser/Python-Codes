
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
    
def insertatI_recursive(head,i,data):
    if (head is None):
        return None
    
    if (i == 0):
        newNode = Node(data)
        newNode.next = head
        return newNode
        
    if (i < 0):
        return head
    
    head.next = insertatI_recursive(head.next, i-1, data)
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
    
    head = insertatI_recursive(head,i,7)
    printLinkedList(head)
    
    head = insertatI_recursive(head,5,8)
    printLinkedList(head)
    t -= 1