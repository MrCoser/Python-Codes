

class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.pq = []


    def getSize(self):
        return len(self.pq)


    def isEmpty(self):
        return self.getSize() == 0

    
    def getMin(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value


    def __percolateUp(self):
        child = self.getSize() - 1

        while (child > 0):
            parent = (child - 1) // 2
            if (self.pq[child].priority < self.pq[parent].priority):
                self.pq[child], self.pq[parent] = self.pq[parent], self.pq[child]
                child = parent

            else:
                break


    def insert(self,value,priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()


    def __percolateDown(self):
        
        parent = 0
        leftChild = 2*parent + 1
        rightChild = 2*parent + 2
        
        
        while leftChild < self.getSize():
            minIndex = parent
            if self.pq[minIndex].priority > self.pq[leftChild].priority:
                minIndex = leftChild
                
                
            if ((rightChild < self.getSize()) and (self.pq[minIndex].priority > self.pq[rightChild].priority)):
                minIndex = rightChild
                
            if minIndex == parent:
                break
                
                
            self.pq[parent], self.pq[minIndex] = self.pq[minIndex], self.pq[parent]
            parent = minIndex
            leftChild = 2*parent + 1
            rightChild = 2*parent + 2
                
                
        
        
        
        
        
    def removeMin(self):
        #############################
        # PLEASE ADD YOUR CODE HERE #
        #############################
        
        if (self.isEmpty() is True):
            return None
        
        res = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        
        self.pq.pop()
        self.__percolateDown()
        
        return res


pq = PriorityQueue()
pq.insert(10,5)
pq.insert(20,7)
pq.insert(25,10)

