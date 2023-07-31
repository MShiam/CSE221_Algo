#!/usr/bin/env python
# coding: utf-8

# In[3]:


#task=01
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\input1.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\output1.txt","w")
nk=int(file.readline())
l_max=[]
l_to_sort_key=[]
for i in range(nk):
    nk2=file.readline().split()
    l_max.append(nk2)
storage_dict={}
for i in l_max:
        storage_dict[i[0]]=i[1]
for i in storage_dict.keys():
    if i!=str(0):
       l_to_sort_key.append(i)
l_to_sort_key.sort()
c=0
for i in l_to_sort_key:
    c+=1
file2.write(f'{str(c)}'"\n")
for i in l_to_sort_key:
    if i in storage_dict:
        #print(i,storage_dict[i])
        file2.write(f'{i} {storage_dict[i]}' "\n")   


# In[ ]:





# In[ ]:




