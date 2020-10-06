# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:31:27 2020

@author: RAMPRIYAN
"""

import collections

option=int(input("Enter the option(1 or 0):"))

if option==1:
    dict1={'day1':'Monday','day2':'Thuesday','day3':'Wednesday'}
    dict2={'day4':'Thursday','day5':'Friday','day6':'Saturday'}

    res=collections.ChainMap(dict1,dict2)

    print(res.maps,'\n')

    print('Keys:{}'.format(list(res.keys())))
    print('Values:{}'.format(list(res.values())))
    print()

    print("Elements:")
    for keys,values in res.items():
        print('{} : {}'.format(keys,values))
        print()


    test_data=input(str("Enter the day:"))
    result=test_data in res
    if result:
        print("You type a existing data")
    else:
        print("Opps! please enter correct data ")
        print("Bye! Bye!")
    """print('day2 in res:{}'.format('day2' in res))
print('day7 in res:{}'.format('day7' in res))"""