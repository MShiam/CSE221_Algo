#!/usr/bin/env python
# coding: utf-8

# In[26]:


file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\input3.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab06n\output3.txt","w")
nk=file.readline()
mk = file.readline().split()
lk = file.readline()
storage=[]
for i in mk:
  storage.append(int(i))
storage.sort()
str_1=[]
str_2=[]
output=''
jacount,jicount=0,0
for i in lk:
    check="J"
    if i!=check:
        get = str_1.pop()
        str_2.append(get)
        outp+=str(get)
        jicount+= get
    elif i==check:
        got = storage.pop(0)
        jacount+= got
        str_1.append(got)
        output+= str(got)
#print(output)
file2.write(f'{output}'"\n")
file2.write(f"Jack will work for {jacount} hours" "\n")
file2.write(f"Jill will work for {jicount} hours" "\n")


# In[ ]:





# In[ ]:





# In[ ]:




