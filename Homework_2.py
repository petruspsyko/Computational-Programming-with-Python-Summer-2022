# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:49:17 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"  

class Interval:
    def __init__(self,real_left,real_right=None): #we have set a default value for real_right 
        if isinstance(real_left,complex):
            raise TypeError("Wrong type!")
        elif isinstance(real_right,complex):
            raise TypeError("Wrong type!")
        #elif real_left > real_right:
        #    raise TypeError("The interval must ascend!")
        self.real_left=real_left
        self.real_right=real_right if real_right is not None else real_left
    
    "Task 2"
    #addition
    def __add__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L1+L2,R1+R2)
    
    def __radd__(self, other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L2+L1,R2+R1)

    def __repr__(self):
        return f'[{self.real_left},{self.real_right}]'
    #subtraction
    def __sub__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L1-R2,R1-L2)
        
    def __rsub__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(L2-R1,R2-L1)
    #multiplication
    def __mul__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            return Interval(min([L1*L2,L1*R2,R1*L2,R1*R2]),max([L1*L2,L1*R2,R1*L2,R1*R2]))
    #division
    def __truediv__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            if L2==0 or R2==0:
                raise TypeError("It's not possible to divide by an interval containing zero!")
            elif min([L1/L2,L1/R2,R1/L2,R1/R2]) - max([L1/L2,L1/R2,R1/L2,R1/R2]) <= -10**100:
                raise TypeError("The result is an infinitely large interval :)")
            else:
                return Interval(min([L1/L2,L1/R2,R1/L2,R1/R2]),max([L1/L2,L1/R2,R1/L2,R1/R2]))        
    
    "Task 5"
    
    def __contains__(self,item):
        if self.real_left <= item <= self.real_right:
            return True
        else:
            return False
        
#q=Interval(1.0,4.0)
#print(5 in q)
                      
#example run with two intervals
#q=Interval(1.,10.)
#z=Interval(10**-100,4.) 
#print(q/z)   
        
"Task 3"
#Included in task 2. See "__repr__".

"Task 4"

I1=Interval(1,4)
#print(I1)
I2=Interval(-2,-1)
#print(I2)
#print(I1+I2)
#print(I1-I2)
#print(I1*I2)
#print(I1/I2)

"Task 6"
#contained in Task 2

"Task 7"
#See Task 2 under __init__.



      
    
    