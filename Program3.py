# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:07:42 2019

@author: Sukanya


Python Program to input a year with century and check if it is Leap Year or print invalid if it is not in the form of year with century

"""
print("Enter a year with century to check it is Leap Year or not")
x = int(input())
if x%4 == 0:
    output_msg = "{} is a Leap Year."
    print(output_msg.format(x))
else :
    output_msg = "{} is not a Leap Year."
    print(output_msg.format(x))

