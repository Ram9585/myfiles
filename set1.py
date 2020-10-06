# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:56:35 2020

@author: RAMPRIYAN
"""

days=set(["Mon","Thus","Tues","Fri","Sat","Wed"])
months={"Jan","Mar","Jun"}
dates={22,23,17}
days.add("Sun")
days.discard("Thus")
for day in days:
    print(day)