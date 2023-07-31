#!/usr/bin/env python
# coding: utf-8

# In[6]:


#task-3
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input3.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output3.txt","w")
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
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        file2.write(f'{node} ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, '1')


# In[ ]:





# In[ ]:




