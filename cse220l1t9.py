# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:05:30 2021

@author: My Baby
"""
def pal(ar,size,n):
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
        s=0
        e=size-1
        while(s<e):
            if(ar[s]!=ar[e]):
                return False
            s+=1
            e=+1
       
        return True


    
a=[10,20,0,0,0,10,20,30]
size=5
n=5
print(pal(a,size,n))