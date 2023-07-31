#!/usr/bin/env python
# coding: utf-8

# In[8]:


#task-4
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input4.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output4.txt","w")
r=file.readline().split()
ran=int(r[0])+1
ran2=int(r[1])
lk=[]
lk2=[]
d={}
for i in range(ran):
    lk.append(str(i))
for i in range(ran2):
    nk=file.readline().split()
    lk2.append(nk)
for i  in range(len(lk2)):
     if lk2[i][0] not in d.keys():
            d[lk2[i][0]]=lk2[i][1:]
     else:
        d[lk2[i][0]].append(lk2[i][-1])
graph=d
color={}
parent={}
for u in graph:
    color[u]="w"
    parent[u]=None
def dfs(u,color,parent):
    color[u]='G'
    for v in graph[u]:
        if v=='W':
            cycle=dfs(v,color,parent)
            if cycle==True:
                return 'Yes'
        elif color[v]=='G':
            return 'Yes'
    color[u]='B'
    return False
cyclic='No'
for u in graph.keys():
    if graph[u]=='w':
        cyclic=dfs(u,color,parent)
        if cylic=='Yes':
            break
file2.write(cyclic)


# In[ ]:





# In[ ]:




