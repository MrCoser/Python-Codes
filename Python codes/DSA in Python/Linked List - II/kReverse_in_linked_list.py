
# Online Python - IDE, Editor, Compiler, Interpreter


# def kReverse(head, k) :
# 	#Your code goes here
       
#     if head is None or head.next is None :
#         return head
    
#     current = head
#     next = None
#     prev = None
#     count = 0
 
#     # Reverse first k nodes of the linked list
#     while(current is not None and count < k):
        
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#         count += 1
 
#     # next is now a pointer to (k+1)th node
#     # recursively call for the list starting
#     # from current. And make rest of the list as
#     # next of first node
#     if next is not None:
#         head.next = kReverse(next, k)
 
#     # prev is new head of the input list
#     return prev




from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def kReverse(head, k) :
    if k == 0 or k == 1 :
        return head

    current = head
    fwd = None
    prev = None

    count = 0

    #Reverse first k nodes of linked list 
    while (count < k) and (current is not None) :
        
        fwd = current.next
        current.next = prev
        prev = current
        current = fwd
        count += 1


    if fwd is not None :
        head.next = kReverse(fwd, k)
    
    return prev



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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1