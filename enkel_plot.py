# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 08:19:51 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

x_axel=linspace(-50,50,100)
y_axel=[]
def f(x):
    return 3*x**2+x+3
for i in x_axel:
    y_axel.append(f(i))
    
plot(x_axel,y_axel)
    