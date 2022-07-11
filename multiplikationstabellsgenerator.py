# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 08:10:55 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

numbers=[1,2,3,4,5,6,7,8,9,10]
myfile=open('numbers.txt','w')
for i in numbers:
    myfile.write(f"{i} gånger 10^-3 blir {i*10**-3}\n")
    
myfile.close()