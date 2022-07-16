# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 07:16:50 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"

# Define polynomial of degree 3
def f(x): 
    return x**3+2*x**2+x+1

# Define derivative
def slope(x): #ger lutningen k
    return 3*x**2+4*x+1

"Task 2"

# Define x data range for polynomial
x = linspace(-5,5,100)

# Choose point to plot tangent line
x1 = 2
y1 = f(x1)

# Define tangent line
# y = k*(x - x1) + y1
def line(x, x1, y1):
    return slope(x1)*(x - x1) + y1 #det här är vad som kallas enpunktsformeln.

# Define x data range for tangent line
xrange = linspace(x1-2, x1+2, 10)

# Plot the figure

fig1,ax1=subplots()
ax1.plot(x,f(x),label = '$x^3+2x^2+x+1$')
ax1.plot(x,slope(x),label = '$3x^2+4x+1$')
ax1.legend(loc = 'lower center', fontsize = 'small')#för att få med label i grafen, placering

fig1.savefig("my_figure_1.png") #sparar som npg

fig2, ax2=subplots()
ax2.plot(x, f(x))
scatter(x1, y1, color='green', s=50) #plottar punkten
ax2.plot(xrange, line(xrange, x1, y1), 'green', linewidth = 2)
xlabel('x')
ylabel('y')
xlim(-4,4)
title('Tangent i kurvan $f(x)=x^3+2x^2+1$')
ax2.set_xticks([2]) # för att ange vissa viktiga värden
ax2.set_xticklabels(['$f(2)$'])
annotate("$tangent$",xy = (3,40),xytext=(2.5,150),arrowprops={'facecolor':'green','shrink':0.05,'width':0.3})
#shrink gör pilen kortare

fig2.savefig("my_figure_2.png") #sparar som npg