# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:06:37 2020

@author: RAMPRIYAN
"""
import collections

dict1={'day1':'Monday','day2':'Thuesday'}
dict2={'day3': 'Wednesday','day4':'Thursday'}

res=collections.ChainMap(dict1,dict2)
print(res.maps,'\n')

print('Keys:{}'.format(list(res.keys())))
print('Values:{}'.format(list(res.values())))
print()

print('Elements:')

for key,value in res.items():
    print('{} : {}'.format(key,value))
print()

print('day3 in res:{}'.format('day3' in res))
print('day4 in res:{}'.format('day4' in res))
