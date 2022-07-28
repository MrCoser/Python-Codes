
# Online Python - IDE, Editor, Compiler, Interpreter

class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
        #Implement the getMax() function here
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
    
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
        
        #Implement the insert() function here
    def __percolateDown(self):
        pi = 0
        lci = 1
        rci = 2
        while lci<self.getSize():
            mi = pi
            if self.pq[mi].priority<self.pq[lci].priority:
                mi = lci
            if rci<self.getSize() and self.pq[mi].priority<self.pq[rci].priority:
                mi = rci
            if mi == pi:
                break
            self.pq[pi],self.pq[mi] = self.pq[mi],self.pq[pi]
            pi = mi
            lci = pi*2 + 1
            rci = pi*2 + 2
        
    def removeMax(self):
        if self.isEmpty():
            return None
        max = self.pq[0].ele
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return max
        #Implement the removeMax() function here
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1