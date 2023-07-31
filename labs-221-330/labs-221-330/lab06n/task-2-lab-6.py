#!/usr/bin/env python
# coding: utf-8

# In[2]:


#task-02
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\input2.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\output2.txt","w")
nk=file.readline().split()
ran=int(nk[0])
d={}
for i in range(ran):
    nk2=file.readline().split()
    if nk2[1] not in d.values():
        d[nk2[0]]=nk2[1]
count=len(d) 
file2.write(str(count))


# In[ ]:




