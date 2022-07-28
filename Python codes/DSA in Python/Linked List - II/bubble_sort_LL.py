
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


        
def length(head):
    #Your code goes here
    count = 0
    curr = head
    
    while(curr):
        count = count + 1
        curr = curr.next
        
    return count

def bubbleSort(head) :
	#Your code goes here
    
    count = length(head)
    for i in range(count - 1):
        curr = head
        nxt = head.next
        prev = None
        
        while nxt:   #Comparisons in passes
            if (curr.data > nxt.data):
                if prev == None:
                    prev = curr.next
                    nxt = nxt.next
                    prev.next = curr
                    curr.next = nxt
                    head = prev
                
                else:
                    temp = nxt
                    nxt = nxt.next
                    prev.next = curr.next
                    prev = temp
                    temp.next = curr
                    curr.next = nxt
                    
            else:
                prev = curr
                curr = nxt
                nxt = nxt.next
    
    return head

def swap(a,b):
    tmp = b.next
    b.next = a
    a.next = tmp
    
    return b








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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)