# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:30:31 2019

@author: Sukanya

Python program to input a month name to print number of days in it.

"""
mydict = {"January":"31","February" : "28/29" ,"March" : "31" , "April" : "30" , "May" : "31" , "June" : "30" , "July" : "31" , "August" : "31" , "September" : "30" , "October" : "31" , "November" : "30" , "December" : "31" }
month = input("Enter month name to get number of days")
print("Number of days in "+month+" : "+mydict[month])
