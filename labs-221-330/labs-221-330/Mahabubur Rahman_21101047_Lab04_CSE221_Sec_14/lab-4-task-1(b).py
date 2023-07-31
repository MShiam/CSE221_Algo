#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task-1-b
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input1-b.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output1-b.txt","w")
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
            d[lk2[i][0]]=[lk2[i][1:]]
     else:
        d[lk2[i][0]].append(lk2[i][1:])
for i in lk:
    if i in d.keys():
        if len(d[i])>1:
            k1=d[i][0]
            k2=d[i][1]
            val1=tuple(k1)
            val2=tuple(k2)
            file2.write(f"{i}:{val1}{val2}\n")
        else:
            k3=d[i][0]
            val3=tuple(k3)
            file2.write(f"{i}:{val3}\n")
    else:
        file2.write(f'{i}:\n')


# In[ ]:




