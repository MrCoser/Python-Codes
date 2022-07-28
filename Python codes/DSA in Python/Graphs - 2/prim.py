
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an undirected, connected and weighted graph G(V,E)
# with V number of vertices (numbered from 0 to V-1) and 
# E number of edges.
# 
# Find and print the Minimum Spanning Tree (MST) using 
# Prim's Algorithm.


## Read input as specified in the question.
## Print output as specified in the question.

import sys

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
    
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
        
    def _str_(self):
        return str(self.adjMatrix)
    
    
    
    def __getMinVertex(self,visited, weight):
        
        min_vertex = -1
        
        for i in range(self.nVertices):
            if ((visited[i] is False) and ((min_vertex == -1) or (weight[min_vertex] > weight[i]))):
                
                min_vertex = i
        return min_vertex
                
    
    
    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0
        
        
        for i in range(self.nVertices - 1):
            
            min_vertex = self.__getMinVertex(visited, weight)
            visited[min_vertex] = True
            
            
            
            for j in range(self.nVertices):
                
                if ((self.adjMatrix[min_vertex][j] > 0) and (visited[j] is False)):
                    if (weight[j] > self.adjMatrix[min_vertex][j]):
                        
                        weight[j] = self.adjMatrix[min_vertex][j]
                        parent[j] = min_vertex
                        
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
                
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))
    
    

# main
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)

for i in range(e):
    arr = [int(y) for y in input().split()]
    u = arr[0]
    v = arr[1]
    w = arr[2]
    g.addEdge(u,v,w)
    
    
g.prims()