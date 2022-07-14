# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 08:41:51 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

class Point:
    def __init__(self, x, y=None):
        self.x = x
        self.y = y if y is not None else x
     
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

print(Point(1))
print(Point(1, 2))
