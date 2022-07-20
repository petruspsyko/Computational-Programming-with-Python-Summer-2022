# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:36:13 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

fig = figure()

sld_ax = axes([0.28, 0.9, 0.6, 0.05])  # axes for slider
plt_ax = axes([0.14, 0.15, 0.8, 0.7])  # axes for the plot

# Här skapar vi slidern

sld = Slider(sld_ax, 'Värdet på $\omega$ i $Sin(\omega x)$', -4, 4,valinit=0.,valstep=0.2)

# Här skapar vi plotten

x = linspace(-pi, pi, 200) # x-värden för plotten
plt_ax.set_ylim(-1., 1.) # sätter värden på y-axeln i plotten
plt_ax.grid()
plt_ax.set_xlabel('Sin(x)')
plt_ax.set_ylabel('Sin(x)=y')
plt_ax.set_xticks([-pi,0,pi])
plt_ax.set_xticklabels(['$-\pi$','$0$','$\pi$'])

lines, = plt_ax.plot(x, sin(sld.val*x))


def update_amplitude(val): # val är ett attribut till sld (Slider)
    lines.set_ydata(sin(sld.val*x))
    
sld.on_changed(update_amplitude) # executes update_amplitude-funktionen

show()