# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:38:02 2021

@author: My Baby
"""
def compare(a1,a2,size1,size2,start1,start2):
    c=0
    max=0
    for i in range(0,len(a1)):    
        for j in range(0,len(a2)):
            if(a1[i]==a2[j]):
                c+=1
        if(c>max):
            max=c
    return c

a1=[10,20,0,0,0,10,20,30]
size1=5
start1=5
a2=[30,20,0,0,0,10,20,30]
size2=5
start2=5
print(compare(a1,a2,size1,size2,start1,start2))
