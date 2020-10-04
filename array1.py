# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 06:22:09 2020

@author: RAMPRIYAN
"""

from array import*
arr1=array('i',[12,34,54,32,11,76])
arr1.insert(6,79)
arr1.remove(12)
arr1[0]=98
print(arr1.index(32))

for i in arr1:
    print(i)
    