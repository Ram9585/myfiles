# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 06:54:03 2020

@author: RAMPRIYAN
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add(self,data):
        
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.add(data)
       
        elif data > self.data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.add(data)
        else:
            self.data=data
    def search(self,val):
        if val==self.data:
            return True
        if val<self.data:
            if self.left: 
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()
            
root=Node(15)
root.add(12)
root.add(27)
root.add(7)
root.add(20)
root.add(88)
root.add(14)
root.add(23)
print(root.search(15))
print(root.search(12))
print(root.search(27))
print(root.search(7))
print(root.search(20))
print(root.search(88))
print(root.search(14))
print(root.search(23))
print(root.search(11))
print(root.search(16))
root.display()

                
        