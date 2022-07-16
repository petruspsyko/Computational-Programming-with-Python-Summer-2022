# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:43:08 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
#from matplotlib.widgets import Slider

fig = figure()

sld_ax = axes([0.2, 0.9, 0.6, 0.05])  # axes for slider
plt_ax = axes([0.1, 0.15, 0.8, 0.7])  # axes for the plot

# Här skapar vi slidern

sld = Slider(sld_ax, 'Amplitude', 0., 5.,valinit=1.,valstep=0.2)

# Här skapar vi plotten

x = linspace(-2*pi, 2*pi, 200) # x-värden för plotten
plt_ax.set_ylim(-5.5, 5.5) # sätter värden på y-axeln i plotten 

lines, = plt_ax.plot(x, sld.val*sin(x))

# callback function

print(sld.val) # printar init-värdet

def update_amplitude(val): # val är ett attribut till sld (Slider)
    if val < 3.5:
        lines.set_color('red') # röd linje om värdet under 3.5
    else:
        lines.set_color('blue')
    lines.set_ydata(val*sin(x))
    
# lines.get_ydata(), om du vill veta vad som finns i lines (collection of points).
    
sld.on_changed(update_amplitude) # executes update_amplitude-funktionen

show()