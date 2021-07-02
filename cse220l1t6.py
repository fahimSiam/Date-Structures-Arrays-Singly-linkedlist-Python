# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:33:57 2021

@author: My Baby
"""


def array(k):
    ar=[0]*k*k
    n=1
    i=(k*k)-1
    p=k
    while(i>0):
        if(n>k):
            n=1
            p-=1
        if(n>p):
            ar[i]=0
        else:
            ar[i]=n
        n+=1
        i-=1
    return ar


k=int(input("number"))
ar=array(k)
for l in range(0,len(ar)):
    print(ar[l])