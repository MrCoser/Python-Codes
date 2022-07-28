
# Online Python - IDE, Editor, Compiler, Interpreter


from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    # Your code goes here
    stack = []
    while(not inputQueue.empty()):
        stack.append(inputQueue.queue[0])
        inputQueue.get()
        
    while(len(stack) != 0):
        inputQueue.put(stack[-1])
        stack.pop()








'''-------------- Utility Functions --------------'''



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1