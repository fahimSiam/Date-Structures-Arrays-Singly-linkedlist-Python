# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:39:36 2021

@author: My Baby
"""

def repitation(a):
    doubleNum=0
    arr=[]
    a.sort()
    prev=-9999
    for i in a:
        if prev!=i and a.count(i)>=2:
            arr.append(a.count(i))
            prev=i
    # print(doubleNum)
    for i in arr:
        if arr.count(i)>=2:
            return True
        else:
            return False

a=[1,3,2,3,3,5,2,2]
print(repitation(a))