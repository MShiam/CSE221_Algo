#!/usr/bin/env python
# coding: utf-8

# In[10]:


#short path
#task-5
from queue import Queue
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input5.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output5.txt","w")
k=file.readline().split()
find=k[-1]
ran=int(k[1])
lstore=[]
d={}
for i in range(ran):
    nk=file.readline().split()
    lstore.append(nk)
for i in range(len(lstore)):
     if lstore[i][0] not in d.keys():
            d[lstore[i][0]]=[lstore[i][1]]
     else:
        d[lstore[i][0]].append(lstore[i][1])
     if lstore[i][1] not in d.keys():
            d[lstore[i][1]]=[lstore[i][0]]
     else:
        d[lstore[i][1]].append(lstore[i][0])
graph=d
visited={}
distance={}
parent={}
out=[]
s='1'
queue=Queue()
for i in graph.keys():
    visited[i]=False
    parent[i]=None
    distance[i]=-1
visited[s]=True
distance[s]=0
parent[s]=None
queue.put(s)
while  not queue.empty():
    u=queue.get()
    out.append(u)
    for v in graph[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            distance[v]=distance[u]+1
            queue.put(v)
v=find
path=[]
d=distance[v]
while find is not None:
    path.append(find)
    find=parent[find]
path.reverse()
for i in range(len(path)):
    if path[-1]==path[i]:
        p=path[i]
        file2.write(f'{p}\n')
    else:
        p2=path[i]
        #print(path[i],end=",")
        file2.write(f'{p2}, ')
file2.write(f'{d}')


# In[ ]:





# In[ ]:




