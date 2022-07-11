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
        if isinstance(real_left,complex):
            raise TypeError("Wrong type!")
        elif isinstance(real_right,complex):
            raise TypeError("Wrong type!")
        elif real_left > real_right:
            raise TypeError("Wrong order!")
        self.real_left=real_left
        self.real_right=real_right
        
    "Task 2"
    
    def __add__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L1+L2,R1+R2)
        #else:
            #Interval(self.real_left,self.real_right)+other #förstår inte varför detta inte funkar
    
    def __radd__(self, other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L2+L1,R2+R1)
        #else:
            #Interval(self.real_left,self.real_right)+other
    
    def __repr__(self):
        return f'[{self.real_left},{self.real_right}]'

#example run with two intervals
z=Interval(3.,6.)
q=Interval(3.,4.) 
print(z+q)                    