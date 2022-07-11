# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 07:30:50 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

x=0.5
a=0.5
for i in range(200):
    x=sin(x)-a*x+30
    if  20 < x < 21:
        break
    else:
        print(f'The result after {i+1} iterations is {x}')



        


