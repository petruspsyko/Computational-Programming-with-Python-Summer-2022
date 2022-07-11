# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:09:05 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"

class ComplexNumber:
    def __init__ (self,real_part,imaginary_part):
        self.re=real_part
        self.im=imaginary_part

    "Task 2"

    #add two complex numbers
    def addComplexNumbers(self,other):
        r1,z1=self.re,self.im
        if isinstance(other,ComplexNumber):
            r2,z2=other.re,other.im
            return ComplexNumber(r1+r2,z1+z2)
        else: 
            self.re + other

    def __radd__(self,other):
        r1,z1=self.re,self.im
        if isinstance(other,ComplexNumber):
            r2,z2=other.re,other.im
            return ComplexNumber(r2+r1,z2+z1)
        else:
            other+self.re
    
    def __repr__(self):
        return f'{self.re}+i{self.im}'
   
    #power of complex numbers
    def complexPowers(self,other):
        r1,z1=self.re,self.im
        if isinstance(other,ComplexNumber):
            p=int(other)
            return ComplexNumber(r1,z1)

#z=ComplexNumber(3,5)
#q=ComplexNumber(4,9)

#print(addComplexNumbers(z,q))


