# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:52:03 2021

@author: My Baby
"""
def shiftLeft(ar,n):
        j=0
        for i in range(n,len(ar)):
                ar[j]=ar[i]
                j+=1
        for k in range(len(ar)-n,len(ar)-1):
            ar[k]=0
        return ar
        
        
source=[10,20,30,40,50,60]
a=3
source=shiftLeft(source,a)
for l in range(0,len(source)-a):
    print(source[l])
    