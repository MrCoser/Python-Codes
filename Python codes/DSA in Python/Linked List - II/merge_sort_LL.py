
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


        
# Utility function to get the middle of the linked list
def getMiddle(head):
    if (head == None):
        return head
 
    slow = head
    fast = head
 
    while (fast.next != None and
             fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
             
    return slow
    
def merge(left, right):
    
    result = None
    
    if left is None:
        return right
    
    if right is None:
        return left
    
    # pick either a or b and recur..
    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
        
    else:
        result = right
        result.next = merge(left, right.next)
        
    return result
    
    
    
def mergeSort(head) :
	#Your code goes here
    
    if head is None or head.next is None:
        return head
    
    
    mid = getMiddle(head)
    
    head1 = head
    head2 = mid.next
    mid.next = None
    
    left = mergeSort(head1)
    right = mergeSort(head2)
    
    sort = merge(left, right)
    return sort





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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1