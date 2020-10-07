# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 07:18:56 2020

@author: RAMPRIYAN
"""
def recursion(k):
    if k > 0:
        result=k + recursion(k-1)
        print(result)
    else:
        result=0
    return result
recursion(6)