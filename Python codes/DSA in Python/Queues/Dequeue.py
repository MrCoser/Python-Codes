
# Online Python - IDE, Editor, Compiler, Interpreter

## Read input as specified in the question.
## Print output as specified in the question.
class Deque:
    def __init__(self, size):
        self.dq = [0 for i in range(size)]
        self.n = size
        self.front = -1
        self.rear = -1

    def pushFront(self, x):
        if(self.isFull() == True):
            print(-1)
            return 
        if(self.isEmpty() == True):
            self.front = self.rear = 0
        else:
            if (self.front == 0):
                self.front = self.n-1
            else:
                self.front -= 1

        self.dq[self.front] = x
        

    def pushRear(self, x):
        if(self.isFull() == True):
            print(-1)
            return
        if(self.isEmpty() == True):
            self.front = self.rear = 0
        else:
            if (self.rear == self.n-1):
                self.rear = 0
            else:
                self.rear += 1

        self.dq[self.rear] = x
        
    def popFront(self):
        if(self.isEmpty() == True):
            print(-1)
            return -1

        item = self.dq[self.front]

        if(self.front == self.rear):
            self.front = self.rear = -1
        else:
            if (self.front == self.n-1):
                self.front = 0
            else:
                self.front += 1

        

    def popRear(self):
        if(self.isEmpty() == True):
            print(-1)

        item = self.dq[self.rear]

        if(self.front == self.rear):
            self.front = self.rear = -1
        else:
            if (self.rear == 0):
                self.rear = self.n-1
            else:
                self.rear -= 1

        


    def getFront(self):
        if(self.isEmpty() == True):
            return -1
        return self.dq[self.front]


    def getRear(self):
        if(self.isEmpty() == True):
            return -1
        return self.dq[self.rear]

    def isEmpty(self):
        if(self.front == -1):
            return True
        return False

    def isFull(self):
        if ((self.front == 0 and self.rear == self.n - 1) or (self.front == self.rear + 1)):
            return True
        return False


n = input().strip().split(" ") 
i = 0
de = Deque(10)
while i < len(n):
    x = int(n[i])
    if x == 1:
        data = int(n[i+1])
        de.pushFront(data)
        i = i + 2
    if x== 2:
        data = int(n[i+1])
        de.pushRear(data)
        i = i + 2
    if x== 3:
        de.popFront()
        i = i + 1
    if x == 4:
        de.popRear()
        i = i + 1
    if x == 5:
        print(de.getFront())
        i = i + 1
    if x == 6:
        print(de.getRear())
        i = i + 1
    if x == -1:
        break