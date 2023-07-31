#!/usr/bin/env python
# coding: utf-8

# In[10]:


#task-5
import heapq
file1=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\input5.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-5\output5.txt","w")
def Network(graph,s):
    Q=[]
    dist={}
    dist[s]=float('inf')
    parent={}
    visited=[False for i in range(len(graph)+1)]
    for v in graph:
        if v!=s:
            dist[v]=float('-inf')
        parent[v]=None

    heapq.heappush(Q,s) 
    while Q!=[]:
        u=heapq._heappop_max(Q)
        if visited[u]:
            continue
        visited[u]=True
        for v,w_uv in graph[u].items():
            a=min(dist[u],w_uv)
            if a>dist[v]:
                dist[v]=a
                parent[v]=u
                heapq.heappush(Q,v)
                heapq._heapify_max(Q)
    for x in range(1, len(graph)):
        if dist[x] == float('-inf'):
            dist[x] = -1
    dist[s] = 0
    lst=[]
    for y in range(1,len(graph)+1):
        lst.append(dist[y])
    return lst

for i in range(int(file1.readline())):
    s=[int(i) for i in file1.readline().split(' ')]
    if s[1]==0:
        edge={s[0]:{}}
        s=int(file1.readline())
        out=Network(edge,s)
        file2.write(' '.join(str(e) for e in out))
        file2.write('\n')    
        continue
    d={}
    for j in range(s[1]):
        new_l=[int(i) for i in file1.readline().split(' ')]
        d[(new_l[0],new_l[1])]=new_l[2]
    node=[i for i in range(1,s[0]+1)]
    adj_n={v:{} for v in node}
    for (u,v),uv in d.items():
        adj_n[u][v]=uv
    s=int(file1.readline())
    out=Network(adj_n,s)
    file2.write(' '.join(str(e) for e in out))
    file2.write('\n')


# In[ ]:





# In[ ]:




