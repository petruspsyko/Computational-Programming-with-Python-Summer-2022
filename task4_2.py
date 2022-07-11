# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:42:10 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

def fast_approx_ln(x,n):
    a_0 = (1+x)/2                  
    g_0 = sqrt(x)
    A=zeros([n]) # skapar n*n-matris med nollor
    d=a_0 # def d
    D=zeros([n,n])
    
    for k in A:
        d=((2*k+sqrt(x))/2-(4**-k)*k)/1-4**-k
        D[k,k]=d # lägger till d till kolumn k
    
    for i in range(n):           
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 + g_0) # här produceras a_0+i, vilket heter a_0
        A[i]=a_0 # lägg till a_i på plats i
    
    return (x-1)/D[n][n]