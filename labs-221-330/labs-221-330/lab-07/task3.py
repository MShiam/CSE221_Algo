#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task-03
file=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\input3.txt","r")
file2=open("C:\\Users\\MAS COMPUTER\\Desktop\\lab-07\output3.txt","w")
nk=file.read().split()
print(nk)
def solve(s1, s2, s3):
    str_1=len(s1)
    str_2=len(s2)
    str_3=len(s3)
    dp=[[[0 for i in range(str_3 + 1)] for j in range(str_3 + 1)] for k in range(str_1 + 1)]
    for i in range(1,str_1 + 1):
     for j in range(1, str_2 + 1):
        for k in range(1, str_3 + 1):
           if s1[i - 1]==s2[j - 1] == s3[k - 1]:
              dp[i][j][k]=1 + dp[i - 1][j - 1][k - 1]
           else:
              dp[i][j][k]=max(dp[i - 1][j][k],dp[i][j - 1][k],dp[i][j][k - 1])
    return dp[-1][-1][-1]
s1=nk[0]
s2=nk[1]
s3=nk[-1]
ans=solve(s1, s2, s3)
print(ans)
file2.write(str(ans))

