#!/usr/bin/env python
# coding: utf-8

# In[7]:


#task-3
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\input3.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\output3.txt","w")
k=int(file.readline())
l_min=[]
l_max=[]
for i in range(k):
    n_k=file.readline().split()
    if len(n_k)<3:
        ran=int(n_k[-1])
        if ran==0:
            file2.write(str(1)+"\n")
            #print(str(1))
        if ran==1:
            n_k2=file.readline().split()
            alo=""
            alo+=n_k2[0]+'->'+n_k2[1]
            #print((n_k2[-1]))
            file2.write(alo+"\n")
            #print(alo)
            
            
        else:
            for i in range(ran):
                n_k2=file.readline().split()
                l_min=[int(i) for i in n_k2]
                l_max.append(l_min)
                
l=l_max
goal=l[-1][-1]
d={}
nodes=[]
for i in l:
  for j in i:
    if j not in nodes:
      nodes.append(j)
for i in l:
  if i[0] not in d:
    d[i[0]]={i[1]:i[-1]}
  if i[0]  in d:
    d[i[0]].update({i[1]:i[-1]})
for i in nodes:
  if i not in d.keys():
    d[i]={}
d2=sorted(d)
for i,j in d.items():
  d_n={}
  for k,l in j.items():
    new_key=k
    d_n={i:l}
    d[k].update(d_n)
graph=d
import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    parent={vertex: None for vertex in graph}
    pq = [(0, starting_vertex)]
    #print(pq)
    heapq.heappush(pq, (0, starting_vertex))
    #print(pq)
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
    #print(goal)
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]
start=1
distances, parent=calculate_distances(graph,start)
path=make_path(parent,goal)
alo3=''
for i in path:
    if i!=path[-1]:
        k=str(i)
        alo3+=k+"->"
    else:
        k=str(i)
        alo3+=k
        #file2.write(k)
file2.write(alo3)


# In[ ]:





# In[ ]:




