# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:25:24 2019

@author: Sukanya


Python Program to Find the Factorial of a Number.

"""
x = int(input("Enter a number to find a Factorial: "))
fact=1
n=x
output_msg = "Factorial of {} is : {}"
while x > 0 :
    fact=fact*x
    x=x-1
print(output_msg.format(n,fact))
    
    
