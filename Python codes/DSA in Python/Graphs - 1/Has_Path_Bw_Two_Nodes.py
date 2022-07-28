
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin
from collections import defaultdict


# Class for graph using adjacency list representation
class Graph:
    
    def __init__(self, vertex):
        
        self.V = vertex
        self.adjmatrix=[[0 for j in range(vertex)]for i in range(vertex)]
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        
        self.adjmatrix[u][v] = 1
        self.adjmatrix[v][u] = 1
        
        
    def containEdge(self,v1,v2):
        return True if self.adjmatrix[v1][v2] > 0 else False
                
    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
        
    
      
     # Use BFS to check path between s and d
    def hasPath(self, s, d):
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
  
        # Create a queue for BFS
        queue=[]
  
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
  
        while queue:
 
            #Dequeue a vertex from queue
            n = queue.pop(0)
             
            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                   return True
 
            #  Else, continue to do BFS
            for i in range(0,self.V):
                if visited[i] == False and self.adjmatrix[n][i]==1:
                    queue.append(i)
                    visited[i] = True
         # If BFS is complete without visited d
        return False
    
    
    
# main
li = stdin.readline().strip().split()
v=int(li[0])
e=int(li[1])
g=Graph(v)
for i in range(e):
    arr=stdin.readline().strip().split()
    v1=int(arr[0])
    v2=int(arr[1])
    g.addEdge(v1,v2)

arr = [int(x) for x in input().split()]
x = arr[0]
y = arr[1]

if (g.hasPath(x,y)):
    print('true')
    
else:
    print('false')