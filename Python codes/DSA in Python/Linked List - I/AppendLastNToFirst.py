
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def appendLastNToFirst(head, n) :
    #Your code goes here
    temp = head
    t = head
    i = -n
    
    if(head is None):
        return
    
    while (temp.next is not None):
        #When temp went forward n nodes from t
        if (i >= 0):
            t = t.next
        temp = temp.next
        i = i + 1
    
    #Connecting the tail to head
    temp.next = head
    
    #Assigning the new node
    head = t.next
    
    #Deleting the previous condition
    t.next = None
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
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 