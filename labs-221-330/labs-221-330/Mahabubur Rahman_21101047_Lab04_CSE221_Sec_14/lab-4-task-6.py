#!/usr/bin/env python
# coding: utf-8

# In[32]:





# In[51]:


#task-6
import numpy as np
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input6.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output6.txt","w")
line = file.readline().split()
n,e = int(line[0]), int(line[1])
diamonds=[]
for i in range(n):
    read = file.readline().strip()
    nk = [i for i in read]
    diamonds.append(nk)
c_D = np.array(diamonds)
trav=[]
count=[]
i = 0
def u_b(c_D, p, q, q_v):
    try:
        p = (p - 1)
        read = file.readline().strip()
        read=c_D[p][q]
        if [p,q] not in trav:
            if (p >= 0 and q >= 0):
                if c_D[p][q] != "#":
                    trav.append([p,q])
                    q_v.append([p,q])
    except:
        pass
def l_b(c_D, p, q, q_v):
    try:
        p = (p + 1)
        read = file.readline().strip()
        read=c_D[p][q]
        if [p,q] not in trav:
            if p >= 0 and q >= 0:
                if c_D[p][q] != "#":
                    trav.append([p,q])
                    q_v.append([p,q])
    except:
        pass  
def le(c_D, p, q, q_v):
    try:
        q = (q - 1)
        read = file.readline().strip()
        read=c_D[p][q]
        if [p,q] not in trav:
            if p >= 0 and q >= 0:
                if c_D[p][q] != "#":
                    trav.append([p,q])
                    q_v.append([p,q])
    except:
        pass
def ri(c_D, p, q, q_v):
    try:
        q = (q + 1)
        read = file.readline().strip()
        read=c_D[p][q]
        if [p,q] not in trav :
            if  p>=0 and q>=0:
                if c_D[p][q] != "#":
                    trav.append([p,q])
                    q_v.append([p,q])
    except:
        pass
def doT(c_D):
    for i in range(len(diamonds)):
        if "." in c_D[i]:
            for j in range(len(diamonds[i])):
                if c_D[i][j] == ".":
                    return [i,j]
    i = (i + 1)
while (i == 0):
    q_v = [doT(c_D)]
    c = 0
    while True:          
        get = q_v.pop(0)
        try:
            u_b(c_D, get[0], get[1], q_v)
            l_b(c_D, get[0], get[1], q_v)
            le(c_D, get[0], get[1], q_v)
            right(c_D, get[0], get[1], q_v)
            if c_D[get[0]][get[1]] == "D":
                c = (c + 1)
            c_D[get[0]][get[1]]=1
        except:
            i = (i + 1)
        if q_v == []:
            break
    count.append(c)
    max_occurance = max(count)
file2.write(str(max_occurance))


# In[41]:





# In[ ]:




