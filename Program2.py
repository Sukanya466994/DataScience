# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:04:16 2019

@author: Sukanya


Python Program to Check if a Number is Odd or Even by taking user input

"""

print("Enter a number to check it is even or odd")
x = int(input())
if x%2==0:
    output_msg="{} is Even Number"
    print(output_msg.format(x))
else:
    output_msg="{} is Odd Number"
    print(output_msg.format(x))