# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:50:43 2020

@author: RAMPRIYAN
"""
var=1
while var:
    number=int(input("Enter a number:"))
    rev_number=number[::-1]
    
    if rev_number==number:
        print("This number is a palindrome number")
    else:
        print("This number is not a palindrome number")
    