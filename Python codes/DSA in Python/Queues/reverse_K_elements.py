
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    #Your code goes here

    if (inputQueue.empty() == True or 
            inputQueue.qsize() < k):
        return -1
    
    if (k <= 0):
        return -1
    
    Stack = []
 
    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(inputQueue.queue[0])
        inputQueue.get()
 
    # Enqueue the contents of stack
    # at the back of the queue
    while (len(Stack) != 0 ):
        inputQueue.put(Stack[-1])
        Stack.pop()
 
    # Remove the remaining elements and
    # enqueue them at the end of the Queue
    for i in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.queue[0])
        inputQueue.get()
    #check now i have added this
    return inputQueue
 





'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while (qu.empty() is False) :
    print(qu.get(), end = " ")
    