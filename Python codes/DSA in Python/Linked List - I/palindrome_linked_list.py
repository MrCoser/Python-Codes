
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def isPalindrome(head) :
    #Your code goes here
    # Temp pointer
    slow = head
 
    # Declare a stack
    stack = []
     
    ispalin = True
 
    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.data)
         
        # Move ahead
        slow = slow.next
 
    # Iterate in the list again and
    # check by popping from the stack
    while head != None:
 
        # Get the top most element
        i = stack.pop()
         
        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        # Move ahead
        head = head.next
         
    return ispalin

















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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1