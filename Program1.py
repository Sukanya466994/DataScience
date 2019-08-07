# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:48:34 2019

@author: Sukanya

Python program to input a number from the user and check if it is positive, negative or zero. 

"""


print("Enter a number to check it is positive, negative or zero")
x = int(input())
if x>0:
    output_msg="{} is positive number"
    print(output_msg.format(x))
elif x==0:
    output_msg="{} is zero"
    print(output_msg.format(x))
else:
    output_msg="{} is negative number"
    print(output_msg.format(x))
    


