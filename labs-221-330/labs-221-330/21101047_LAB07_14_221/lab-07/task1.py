#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task-01
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\input1.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\output1.txt","w")
l=file.read().split()
s=l[0]
c=0
if len(s)>3:
    print("Invalid")
if len(s)==2 :
    low=int(s[0])
    up=int(s[1])
    k=int(s)
    while k!=0 and len(str(k))!=1:
        if low>up:
           k=k-low
           c+=1
        else:
           k=k-up
           c+=1
if len(s)==3:
    low=int(s[0])
    mid=int(s[1])
    high=int(s[-1])
    k=int(s)
    while k!=0  and len(str(k))!=1:
        if low>mid and low>high: 
           k=k-low
           c+=1
        elif mid>low and mid>high :
           k=k-mid
           c+=1
        else:
           k=k-high
           c+=1
final=c+1
file2.write(str(final))

