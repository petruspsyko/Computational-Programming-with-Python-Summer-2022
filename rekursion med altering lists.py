# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:13:31 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

u=[1,2,3]

for i in range(4):
    u_0=u[2]+(u[2]+u[1]+u[0])
    u[:1]=[] # tar bort första elementet ur u
    u2=[u_0] # def en ny lista med nya elementet u_0
    u=u+u2 # stoppar in u_0 i u
print(u_0)
