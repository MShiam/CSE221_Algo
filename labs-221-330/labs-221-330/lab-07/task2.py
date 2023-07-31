#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task-2
''''Yasnaya Y
 Rozhok R
 School S
 Pochinki P
 Farm F
 Mylta M
 Shelter H
 Prison I'''
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\input2.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\output2.txt","w")
nk=file.read().split()
str1=nk[1]
str2=nk[-1]
def lcs(str1,str2):
    Y="Yasnaya"
    R="Rozhok" 
    S="School"
    P="Pochinki"
    F="Farm"
    M="Mylta"
    H="Shelter"
    I="Prison"
    d={'Y':"Yasnaya","R":"Rozhok" ,"S":"School","P":"Pochinki","F":"Farm","M":"Mylta","H":"Shelter","I":"Prison"}
    a = len(str1)
    b = len(str2)
    string_matrix=[[0 for i in range(b+1)] for i in range(a+1)]   
    for i in range(1,a+1):
        for j in range(1,b+1):
            if i== 0 or j == 0:
                string_matrix[i][j]=0
            elif str1[i-1] == str2[j-1]:
                string_matrix[i][j]=1+string_matrix[i-1][j-1]
            else:
                string_matrix[i][j]=max(string_matrix[i-1][j], string_matrix[i][j-1])
    index=string_matrix[a][b]
    res=[""] * index
    i=a
    j=b
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif string_matrix[i-1][j] > string_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    s=''
    for i in res:
        if i in d.keys():
            s+=d[i]+' '
    #print(s)
    file2.write(s)
    file2.write("\n")
    #Correctness = (Length of longest common zone sequence × 100) ÷ Number of zones

    corre=(len(res)*100)/int(nk[0])
    corre=str(corre)+"%"
    file2.write(corre)
    
                 
check=lcs(str1, str2)

