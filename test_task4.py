# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:13:39 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

def fast(x,n):
    a0=x*2
    g0=x*3
    for i in range(n):
        a0=(a0+g0)/2 # det här ger oss a_i+1
        g0=(a0*g0)+1 # här har vi a_i+1 och g_i, som ger oss g_i+1
    for k in range(n):
        d=[x*2,a0] # a0 är här a_n, och d_0,0=a0=x*2
        d_0=(d[0]-4**-n*d[1])/1-4**-n # n måste vara nytt för varje iteration!
        
        
        
        d[:1]=[] # tar bort det första elementet ur d
        d2=[d_0] # lägger till d_i+1 till d2
        d=d+d2 # stoppar in d2 längst bak i d
    return (x-1)/n