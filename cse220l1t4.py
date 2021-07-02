# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:43:25 2021

@author: My Baby
"""


def removeAll(ar,s,n):
    k=0
    for a in range(0,s):
        if(ar[a]==n):
            j=a  
            for i in range(j+1,s):
                ar[j]=ar[i]
                j+=1
            k+=1
        for l in range(s-k-1,s):
            ar[l]=0
    return ar


source=[10,2,30,2,50,2,2,0,0]
s=7
n=2
source=removeAll(source,s,n)
for l in range(0,len(source)):
    print(source[l])