
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an undirected, connected and weighted graph G(V, E) with V
# number of vertices (numbered from 0 to V-1) and 
# E number of edges.
# Find and print the Minimum Spanning Tree (MST) using
# Kruskal's Algorithm.


## Read input as specified in the question.
## Print output as specified in the question.

class Edge:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        
        
def getParent(v, parent):
    
    
    if (v == parent[v]):
        return v

    return getParent(parent[v], parent)
    
def kruskal(edges, vertices):
    
    parent = [i for i in range(vertices)]
    edges = sorted(edges, key = lambda  edge:edge.z)
    count = 0
    
    
    output = []
    i = 0
    
    while count < (vertices - 1):
        currEdge = edges[i]
        src = getParent(currEdge.x, parent)
        dest = getParent(currEdge.y, parent)
        
        if src != dest:
            
            output.append(currEdge)
            count += 1
            parent[src] = dest
            
        i += 1
        
    
    return output
    
        
        
# main
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]

edges = []

for i in range(e):
    inp = [int(ele) for ele in input().split()]
    ei = inp[0]
    ej = inp[1]
    wi = inp[2]
    edge = Edge(ei,ej,wi)
    edges.append(edge)
    
    
out = kruskal(edges, v)
for ele in out:
    
    if (ele.x < ele.y):
        print(str(ele.x) + " " + str(ele.y) + " " + str(ele.z))

    else:
        print(str(ele.y) + " " + str(ele.x) + " " + str(ele.z))
