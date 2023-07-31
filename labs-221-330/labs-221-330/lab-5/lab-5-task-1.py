#!/usr/bin/env python
# coding: utf-8

# In[3]:


file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\input1.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\output1.txt","w")
k=file.read().split()
j=0
nodes=[]
g={}
for i in range(1,len(k)+1):
    if i%3==0 and i!=0:
        mini=k[j:i]
        #pair=(mini[0],mini[1])
        i=i+1
        j+=3
        nodes.append(mini[0])
        val,key1=int(mini[-1]),mini[0]
        key2=mini[1]
        d1={mini[1]:val}
        d2={mini[0]:val}
        if key1 not in g.keys():
            g[key1]=d1
        else:
            g[key1].update(d1)

nodes=[(i) for i in g.keys()]
s=nodes[0]
missing_nodes=[]
for i,j in g.items():
    for k in j:
        if type(k)!=int and k not in nodes:
            missing_nodes.append(k)
for i in missing_nodes:
    g[i]={}

for i,j in g.items():
    for k in j:
        if k in nodes and k!=s:
            n_val=i
            min_d=g[n_val]
            x=min_d[k]
            n_min_d={n_val:x}
            #print(n_min_d)
            g[k].update(n_min_d)
        if type(k)!=int and k not in nodes:
            n_val=i
            min_d=g[n_val]
            x=min_d[k]
            n_min_d={n_val:x}
            #print(n_min_d)
            g[k].update(n_min_d)
#print(g)
import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    parent={vertex: None for vertex in graph}
    pq = [(0, starting_vertex)]
    #print(pq)
    heapq.heappush(pq, (0, starting_vertex))
    #print(pq)
    goal='MOGHBAZAR'
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor]=current_vertex
                heapq.heappush(pq, (distance, neighbor))
                #parent[neighbor]=current_vertex 
                #print(pq)
    return distances, parent
def make_path(parent, goal):
    print(goal)
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]
distances, parent=calculate_distances(g,'Motijheel')
path=make_path(parent,'MOGHBAZAR')
print(distances)
print(parent)
print(path)
p=''
for i in path:
    if i!=path[-1]:
        p+=i+','
    else:
        p+=i
file2.write(p)


# In[ ]:





# In[ ]:




