
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


#Function to remove all duplicates from a sorted linked list
def removeDuplicates(head) :
    #Your code goes here
    
    
    if (head is None):
        return
    # Do nothing if the list consist of
    # only one element or empty 
    if (head is None or
        head.next is None):
        return
     
    # Construct a pointer
    # pointing towards head
    current = head
     
    # Initialise a while loop till the
    # second last node of the linkedlist
    while (current.next):
         
        # If the data of current and next
        # node is equal we will skip the
        # node between them
        if current.data == current.next.data:
            current.next = current.next.next
             
        # If the data of current and
        # next node is different move
        # the pointer to the next node
        else:
            current = current.next
     
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
t = int(stdin.readline().strip())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1