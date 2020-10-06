# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 06:23:29 2020

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
    def removefromq(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in the queue")
q=Queue()
q.inserttoq("Monday")
q.inserttoq("Thuesday")
q.inserttoq("Wednesday")

print(q.removefromq())
print(q.removefromq())
