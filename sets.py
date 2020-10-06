# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:05:47 2020

@author: RAMPRIYAN
"""

daysA={"Wed","Mon","Fri","Thurs"}
daysB={"Wed","Tues","Sat","Sun"}

AllDays=daysA|daysB # Union of sets

print(AllDays)

daysC={"Mon","Thurs","Fri"}
daysD={"Wed","Sat","Thurs","Thue","Sun"}

AllDaysA=daysC-daysD #Difference of sets

print(AllDaysA)

Intersection_of_days=daysA & daysB # Intersection of sets

print(Intersection_of_days)

Subset_Res=daysA <= daysB  #Check subset
Superset_Res=daysB >= daysA #check superset

print(Subset_Res)
print(Superset_Res)
