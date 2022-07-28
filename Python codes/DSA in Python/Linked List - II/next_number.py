
# Online Python - IDE, Editor, Compiler, Interpreter

## Read input as specified in the question.
## Print output as specified in the question.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def reverseList(head):
    if not head:
        return
    
    curNode = head
    prevNode = head
    nextNode = head.next
    curNode.next = None
  
    while(nextNode):
        curNode = nextNode
        nextNode = nextNode.next
        curNode.next = prevNode
        prevNode = curNode
  
    return curNode
  
# Adds one to a linked lists and return the head
# node of resultant list
  
  
def nextNumber(head):
  
    # Reverse linked list and add one to head
    head = reverseList(head)
    k = head