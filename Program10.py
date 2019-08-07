# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:50:47 2019

@author: Sukanya


Python Program to Find the Sum of Natural Numbers.

"""
n = int(input("Enter number to find sum :"))
sum = 0
if(n < 0) :
    print("Please enter a positive Number")
else:
    sum =( n*(n + 1))/2
    print("Sum of ",n," Natural numbers is :",sum)

