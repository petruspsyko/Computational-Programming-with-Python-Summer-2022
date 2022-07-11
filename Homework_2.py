# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:49:17 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"

class Interval:
    def __init__(self,real_left,real_right):
        self.real_left=real_left
        self.real_right=real_right
        
    "Task 2"
    
    def addIntervals(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L1+R2,L2+R1)

    def __repr__(self):
        return f"self.real_left,self.real_right"                        