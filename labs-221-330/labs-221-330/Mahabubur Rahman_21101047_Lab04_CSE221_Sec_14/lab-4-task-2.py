#!/usr/bin/env python
# coding: utf-8

# In[4]:


#task-2
from queue import Queue
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input2.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output2.txt","w")
k=file.readline().split()
ran=int(k[0])+1
lk=[] #list containing value of keys of  d2
lmax=[]
d={}
d2={}
for i in range(1,ran):
    lk.append(str(i))
for i in range(int(k[1])):
    nK=file.readline().split()
    lmax.append(nK)
for i in lmax:
    if i[0] not in d.keys():
        val=i[1]
        d[i[0]]=[val]
    else:
        val2=i[1]
        d[i[0]].append(val2)
#
for i in lk:
    if i in d.keys():
        d2[i]=d[i]
    else:
        d2[i]=[]
graph=d2
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
path=out
for i in range(len(path)):
    if path[-1]==path[i]:
        p=path[i]
        file2.write(f'{p}\n')
    else:
        p2=path[i]
        #print(path[i],end=",")
        file2.write(f'{p2} ')


# In[ ]:





# In[ ]:




