# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 04:49:07 2020

@author: RAMPRIYAN
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,data):
       if data < self.data:
           if self.left is None:
               self.left=Node(data)
           else:
               self.left.insert(data)
       elif data > self.data:
          if self.right is None:
              self.right=Node(data)
          else:
              self.right.insert(data)
       else:
          self.data=data
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
    def Search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False
            
        

root=Node(12)
root.insert(6)
root.insert(16)
root.insert(3)

print(root.Search(12))

root.printtree()
