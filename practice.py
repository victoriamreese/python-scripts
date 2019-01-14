#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:51:29 2018

@author: vicky
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
	    print(time)

clock = Clock('5:30')
clock.print_time('10:30')