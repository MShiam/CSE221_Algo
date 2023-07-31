#!/usr/bin/env python
# coding: utf-8

# In[4]:


#task-04
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\input4.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\output4.txt","w")
nk=file.read().split()
storage=[]
str_big=[]
for i in nk:
    storage.append(int(i))
for i in range(0,len(storage),2):
    c=0
    for j in range(storage[i],storage[i+1]+1):
        if storage[i]!=0 and storage[i+1]+1<100000 and j**2<=storage[i+1]+1:
            #print(j**2)
            c+=1
    if c!=0:
        file2.write(f"{c}""\n")
    


# In[ ]:




