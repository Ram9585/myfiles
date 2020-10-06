# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 05:26:03 2020

@author: RAMPRIYAN
"""

class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    """def peek(self):
        return self.stack[-1]"""
    def remove(self):
        if len(self.stack) <=0:
            return ("No element in the stack")
        else:
           return self.stack.pop()
    
Asstack=Stack()
Asstack.add("Monday")
Asstack.add("Thuesday")
#Asstack.peek()
#print(Asstack.peek())
Asstack.add("Wednesday")
Asstack.add("Thursday")

#Asstack.peek()
##print(Asstack.peek())
print(Asstack.remove())
print(Asstack.remove())