#!/usr/bin/env python 
# coding: utf-8
 
# In[ ]:
 

n = 4  
e = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]  
m = 3  
def add_edge(graph, u, v):
    while len(graph) <= max(u, v):
        graph.append([])
    graph[u].append(v)
    graph[v].append(u)
def is_safe(graph, v, color, c):
    for i in graph[v]:
        if color[i] == c:
            return False
    return True
def coloring(graph, m, color, v):
    if v == len(graph):  
        return True
    for c in range(1, m + 1):  
        if is_safe(graph, v, color, c):
            color[v] = c 
            if coloring(graph, m, color, v + 1):  
                return True
            color[v] = 0  
    return False
def graph_coloring(n, e, m):
    graph = []  
    for u, v in e: 
        add_edge(graph, u, v)
    color = [0] * n  
    print(color)
    if not coloring(graph, m, color, 0):
        print("Solution does not exist")
        return False
    print("Solution exists: Following are the assigned colors:")
    for c in color:
        print(c, end=' ')
    return True
graph_coloring(n, e, m)


# In[ ]:





# In[ ]:
