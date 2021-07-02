# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:15:39 2021

@author: My Baby
"""

ar=[10, 3, 1, 2, 10]
i=0;
j=len(ar)-1
left=ar[i]
right=ar[j]
while(i<j):
    if(left>right):
        right==right+ar[j-1]
        j=-1
    elif(right>left):
        left==left+ar[i+1]
        i=+1
    else:
        right==right+ar[j-1]
        j=-1
if(left==right):
    print("true")
else:
    print('false')
        