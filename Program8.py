# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:33:05 2019

@author: Sukanya


Python Program to Display the multiplication Table by taking the number as input.

"""
n = int(input("Enter number to display multiplication table: "))
tab_format = "{} * {} = {} \n"
for i in range(1,21):
    print(tab_format.format(i,n,i*n))
    
