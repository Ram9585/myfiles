# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 06:15:54 2020

@author: RAMPRIYAN
"""

class Queue:
    def __init__(self):
        self.queue=list()
    def inserttoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queue)
Q=Queue()
Q.inserttoq("Monday")
Q.inserttoq("Thuesday")
Q.inserttoq("Wednesday")
print(Q.size())