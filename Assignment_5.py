# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:23:29 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad
from scipy import integrate

"Task 1"

def make_sin(w):
    def f(x):
        return sin(w*x)
    return f # ger den lokalt definierade funktionen f

print(quad(make_sin(2*pi),0,pi/2)) # detta fryser w=2*pi

"Task 1: Alt. 2"

w=2*pi
quad(lambda x: sin(w*x), 0, pi/2) # lambda x definierar funktionen och fryser x

"Task 2"

w=linspace(0,2*pi,1000) # ger en lista
integralvalues=[] # en tom lista för att fylla med värden på den integrerade funktionen
for i in w: # går igenom listan w och ger ett nytt värde för varje 
    integralvalues.append(integrate.quad(lambda x: sin(i*x), 0, pi/2))

plot(w,integralvalues)



