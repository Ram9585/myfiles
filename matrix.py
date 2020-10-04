# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 07:14:18 2020

@author: RAMPRIYAN
"""

from numpy import*
a=([['Mon',18,19,20,21],['Tue',25,26,27,28],['wed',30,12,13,14],['Thu',16,17,18,19],['Fri',3,4,7,8],['Sat',5,8,3,9],['Sun',9,10,11,12]])
m=reshape(a,(7,5))
for i in m:
    for j in i:
        print(j,end=' ')
    print()