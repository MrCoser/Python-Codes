
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an undirected, connected and weighted graph G(V,E)
# with V number of vertices (numbered from 0 to V-1) and 
# E number of edges.
# 
# Find and print the shortest distance from the source vertex
# (i.e Vertex 0) to all other vertices (including source vertex also)
# using Djikstra's Algorithm.


import sys
from queue import PriorityQueue

class Graph:

    def __init__(self, nVertices):
    	self.nVertices = nVertices
    	self.adjMatrix = [[0 for i in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2, wt):
    	self.adjMatrix[v1][v2] = wt
    	self.adjMatrix[v2][v1] = wt
        
    
    def __min_vertex(self, visited, distance):
        x = sys.maxsize
        for i in range(self.nVertices):
            if visited[i] == False:
                if distance[i] < x:
                    x = distance[i]
                    a = i
        return a


    def dijkstra(self, start_vertex):
        visited = [False for i in range(self.nVertices)]
        distance = [sys.maxsize for i in range(self.nVertices)]
        distance[0] = 0
        for i in range(self.nVertices - 1):
            min_vertex = self.__min_vertex(visited, distance)
            visited[min_vertex] = True
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    d = distance[min_vertex] + self.adjMatrix[min_vertex][j]
                    distance[j] = min(d, distance[j])
                    
        
        return distance
                    
         
        
li = [int(ele) for ele in input().split()]
n = li[0]
e = li[1]

g = Graph(n)
for i in range(e):
  curr_input = [int(ele) for ele in input().split()]
  g.addEdge(curr_input[0], curr_input[1],curr_input[2])

ans = g.dijkstra(0)
for i in range(len(ans)):
        print(i,ans[i])