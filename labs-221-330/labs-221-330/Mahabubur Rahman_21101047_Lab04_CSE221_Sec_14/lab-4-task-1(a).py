#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task-1-a
l=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\input1.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\Lab4\output1.txt","w")
k=l.readline().split()
r=int(k[0])
r2=int(k[1])
lmax=[]
lmax2=[]
for i in range(r+1):
    lmin=[0]*(r+1)
    lmax.append(lmin)
for i in range(r2):
    nK=l.readline().split()
    lmax2.append(nK)    
for i in lmax2:
  var1=int(i[0])
  for j in range(len(lmax)):
    if j==var1:
      lmax[j][int(i[1])]=int(i[2])
for i in lmax:
    i=[str(x) for x in i]
    file2.write(' '.join(i)+'\n')           


# In[ ]:




