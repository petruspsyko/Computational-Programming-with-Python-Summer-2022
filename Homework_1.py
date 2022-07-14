# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 07:12:13 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"

def approx_ln(x,n): # begins definition of approx_ln(x)
    a0=(1+x)/2 # local def of a0
    g0=sqrt(x) # local def of g0
    for i in range(n): # starts for loop inside of def of function to iterate calc of a n times
        a0=(a0+g0)/2 # a0 is defined locally above, and a_i+1 will be generated from the loop        
        g0=sqrt(a0*g0) # same as above but with g0, and here a0 will be taken from row 15 so it will be a0+1
    return (x-1)/a0 # gives for x in function a value for whatever a0 is after n iterations (note: x is given in call of function outside for loop)

"Task 2: Plot of ln(x) and approx_ln(x,n)"

x_axis1=linspace(0.1,4,200) # I made it 0.1 so that it doesn't go towards negative inf.
y_axis1=[]
for i in x_axis1:
    y_axis1.append(log(i))

x_axis2=linspace(0.1,4,200)
y_axis2=[]
for i in x_axis2:
    y_axis2.append(approx_ln(i,1))

x_axis3=linspace(0.1,4,200)
y_axis3=[]
for i in x_axis3:
    y_axis3.append(approx_ln(i,3)) 
    
plot(x_axis1,y_axis1) # plots ln(x)
plot(x_axis2,y_axis2) # plots approx_ln(x,n), with n=1
plot(x_axis3,y_axis3) # another plot of approx_ln(x,n), for n=3

"Task 2: Plot the difference of the functions"  

def diffunc(x):
    return log(x)-approx_ln(x, 1) # with 1 iteration

x_axis4=linspace(0.1,4,200)
y_axis4=[]
for i in x_axis4:
    y_axis4.append(diffunc(i))

plot(x_axis4,y_axis4)

def diffunc2(x):
    return log(x)-approx_ln(x, 4) # with 4 iterations
x_axis5=linspace(0.1,4,200)
y_axis5=[]
for i in x_axis5:
    y_axis5.append(diffunc2(i))

plot(x_axis5,y_axis5)

"Task 3"

x_axis6=range(60) # so that it is evenly distributed and not cause a problem for diffunc_n(x) with floats
y_axis6=[]

def diffunc_n(x):
    return abs(log(1.41)-approx_ln(1.41,x))

for i in x_axis6:
    y_axis6.append(diffunc_n(i))

plot(x_axis6,y_axis6)

"Task 4"




