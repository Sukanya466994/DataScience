# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:59:00 2019

@author: Sukanya


Python Program to Check if a number is Prime Number or not. 
Also, take the input of a range (min and max) from the user and Print all Prime Numbers that Interval

"""
print("Enter range to find all primenumbers in that interval")
min = int(input("Enter minimum value in interval"))
max = int(input("Enter maximum value of an interval"))
for num in range(min,max + 1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

    
