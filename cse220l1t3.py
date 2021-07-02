# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:19:24 2021

@author: My Baby
"""


def remove(ar,s,n):
    j=n
    for i in range(n+1,s):
        ar[j]=ar[i]
        j+=1
    ar[s-1]=0
    return ar
        
        
source=[10,20,30,40,50,0,0]
s=5
n=2
source=remove(source,s,n)
for l in range(0,len(source)):
    print(source[l])