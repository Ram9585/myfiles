# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:31:06 2020

@author: RAMPRIYAN
"""

class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class sLinkedList:
    def __init__(self):
        self.headval=None
    
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    
    def AtBegining(self,newdata):
        NewNode=node(newdata)
       
        NewNode.nextval=self.headval
        self.headval=NewNode
list=sLinkedList()
list.headval=node("Monday")
e2=node("Thuesday")
e3=node("Wednesday")

list.headval.nextval=e2
e2.nextval=e3

list.AtBegining("Sunday")

list.listprint()