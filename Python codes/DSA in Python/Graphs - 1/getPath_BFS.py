
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adjMatrix)
     
    
    def getPathBFS(self, a, b) :
    
        visited = [False for i in range(self.nVertices)]
        visited[a] = True
        parentDict = {}
        q = queue.Queue()
        q.put(a)
        arr = []
        while q.empty() is False:
            u = q.get()
            if u == b:
                arr.append(u)
                while True:
                    if u not in parentDict:
                        break
                    arr.append(parentDict[u])
                    u = parentDict[u]

            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    visited[i] = True
                    q.put(i)
                    if i not in parentDict:
                        parentDict[i] = u
        return arr  



# Main
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])

li = g.getPathBFS(sv, ev)

if li != None :
    for element in li :
        print(element, end = ' ')