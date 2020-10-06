# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 06:52:40 2020

@author: RAMPRIYAN
"""

import collections

DoubleEnded=collections.deque(["Monday","Thuesday","Wednesday"])

DoubleEnded.append("Thursday")
print("Appended at right-")
print(DoubleEnded)

DoubleEnded.appendleft("Sunday")
print("Appended at left-")
print(DoubleEnded)

DoubleEnded.pop()
print("Deleting from right-")
print(DoubleEnded)

DoubleEnded.popleft()
print("Deleting from left-")
print(DoubleEnded)

