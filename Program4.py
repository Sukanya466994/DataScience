# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:18:56 2019

@author: Sukanya


Python Program to Find the Largest Among Three Numbers, using the least number of lines of code

"""
print("Enter three numbers to find Largest among them")
mylist=[]
output_msg = "{} is Largest among three numbers"
for i in range(0,3):
    ele = int(input())
    mylist.append(ele)
mylist.sort()
print(output_msg.format(mylist[2]))
