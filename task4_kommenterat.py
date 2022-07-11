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
    A=zeros([n,n]) # skapar n*n-matris med nollor
    A[0,0]=a_0 # stoppar in a_0 på första platsen (k,i)
    
    for i in range(1,n): # vi hoppar över element(0,0)           
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 + g_0) # här produceras a_0+i, vilket heter a_0
        A[0,i]=a_0 # lägg till a_i på plats i 
        
    for i in range(1,n):
        
        for k in range(1,n):
            A[i,k]=(A[k-1,i]-((4**-k)*A[k-1,i-1]))/(1-(4**-k))
            
    return (x-1)/A[n-1,n-1]

def difference(x,n):
    return (log(x) - fast_approx_ln(x, n))

x = arange(-50.0, 50.0, 0.1)
y = arange(0,100.0, 0.1)

x = linspace(0.1, 20, 200)
y = []
for i in x:
    y.append(difference(i, 3))

plot(x,y, color="green")
yscale('symlog')
show()