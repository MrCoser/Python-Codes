
# Online Python - IDE, Editor, Compiler, Interpreter

import queue
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix=[[0 for j in range(nvertices)]for i in range(nvertices)]
    def addedge( self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1
                
    def removeedge(self,v1,v2):
        if self.containedge(v1,v2) is False:
            return
        
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
        
    def containedge(self,v1,v2):
        return True if self.adjmatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjmatrix)
    
    def __bfshelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u,end=" ")
            for i in range(self.nvertices):
                if self.adjmatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
    def bfs(self):
        visited=[False for i in range(self.nvertices)]
        for i in range(self.nvertices):
            if visited[i] is False:
                self.__bfshelper(i,visited)               
    
li = stdin.readline().strip().split()
v=int(li[0])
e=int(li[1])
g=graph(v)
for i in range(e):
    arr=stdin.readline().strip().split()
    v1=int(arr[0])
    v2=int(arr[1])
    g.addedge(v1,v2)
g.bfs()
# import collections
# from collections import defaultdict

# class Graph:
#     # This class represents a directed graph
#     # using adjacency list representation
    
#     # Constructor
#     def __init__(self):
#         self.graph = defaultdict(list)
        
#     # function to add an edge to graph    
#     def addEdge(self, x, y):
#         self.graph[x].append(y)
        
       
#     # function for BFS    
#     def BFS(self, s):
        
#         visited = [False] * (max(self.graph) + 1)
        

#         # Create a queue for BFS
#         queue = []
 
#         # Mark the source node as
#         # visited and enqueue it
#         queue.append(s)
#         visited[s] = True
        
#         while queue:
 
#             # Dequeue a vertex from
#             # queue and print it
#             s = queue.pop(0)
#             print (s, end = " ")
 
#             # Get all adjacent vertices of the
#             # dequeued vertex s. If a adjacent
#             # has not been visited, then mark it
#             # visited and enqueue it
#             for i in self.graph[s]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True
                    
                    
                    
                    
                    
# # main
# V = int(input())
# E = int(input())

# g = Graph()

# for i in range(1,(E+1)):
#     a = int(input())
#     b = int(input())
    
#     g.addEdge(a, b)
    
# g.BFS(0)