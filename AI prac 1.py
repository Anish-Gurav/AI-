#!/usr/bin/env python 
# coding: utf-8 

# In[1]:


def bfs(grap, visited, not_visited, node):
    if node not in visited and node in not_visited:
        print(node)
        visited.append(node)
        not_visited.remove(node)
        for neig in graph[node]:
            bfs(graph, visited, not_visited, neig)

    
    
    
def dfs(grap, visited, nod):
    if nod not in visited:
        print(nod)
        visited.append(nod)
        for nei in graph[nod]:
            dfs(graph, visited, nei)
    
    
visited = []  
not_visited = []
graph = {}
vert = int(input("Number of vertices: "))
for i in range(0, vert):
    n = int(input(f"Enter the number of edges for vertex {i}: "))
    l = []
    for j in range(0, n):
        edge = int(input("Enter the neighbour of vertex: "))
        l.append(edge)
    graph[i] = l
    not_visited.append(i)
print(graph)
dfs(graph, visited, 0)
bfs(graph, visited, not_visited, 0)


# In[ ]:





# In[ ]:
