# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 06:48:48 2020

@author: RAMPRIYAN
"""

from array import*
array1=[[35,78,90,24],[36,76,42,56],[67,85,93],[43,48,94]]
array1[0][2]=56
array1[2]=[32,65,32,87]
for i in array1:
    for j in i:
        print(j,end=' ')
    print()
