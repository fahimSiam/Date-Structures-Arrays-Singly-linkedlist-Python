# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:58:30 2021

@author: My Baby
"""


def rotateRight(ar,n):
        j=0
        ar1=[0]*len(ar)
        for l in range(0,len(ar)):
            ar1[l]=ar[l]
        for i in range(n,len(ar)):
            ar[j]=ar[i]
            j+=1
        l=0
        for k in range(len(ar)-n,len(ar)):
            ar[k]=ar1[l]
            l+=1  
        return ar
        
    
source=[10,20,30,40,50,60]
n=3
source=rotateRight(source,n)
for l in range(0,len(source)):
    print(source[l])