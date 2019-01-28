#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:23:40 2019

@author: vicky
"""

#1/22/19 Move Zeroes to the End 

array1 = [9,0.0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
array2 = [0,1,None,2,False,1,0]
array3 = [-6, '0', 0, 6, -1, -2, 10, '0', 10, -4, 0, 'z', -3, 1, 0, 0, 0, -7, -2, 'a', 7, True, False, 5, -6, -10, 2, -8]
def move_zeros(array): 
    non_zeros = [n for n in array if str(n) == '[]' or type(n) == dict or type(n) == bool or type(n) == str or n == None or (type(n) == int and n >0 or n <0) ]
    zeros = [int(n) for n in array if str(n) == '0.0' or str(n) == '0']
    final = non_zeros + zeros
    print(final)
move_zeros(array3)

# False, 0 , 0.0 
#0.0 and 0
    
#or str(n).find('0.') >= 0

#types that are not moved: booleans, strings, numbers greater than 0, nonetype
#prob: nonetype cannot be compared to zero, must be 
n is False


