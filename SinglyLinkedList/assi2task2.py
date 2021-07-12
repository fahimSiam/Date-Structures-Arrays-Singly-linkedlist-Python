# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:11:16 2021

@author: My Baby
"""


class Trace:
    def hMB(self,h):
        if(h==0):
            print("Stop: ",h)
            return 0
        elif(h==1):
            print("Stop: ",h)
            return h
        else:
            print("Continue: ",h)
            return h + self.hMB(h-1)
#Tester
t = Trace()
print("Finally ",t.hMB(5))