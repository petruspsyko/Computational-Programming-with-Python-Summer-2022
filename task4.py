# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 07:30:17 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

def fast_approx_ln(x,n):
    a_0 = (1+x)/2                  
    g_0 = sqrt(x)
    row1=[]
    
    for i in range(n):           
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 + g_0)
        b=(((a_0+g_0)/2)-4**-1*a_0)/1-4**-1 # ger alla a_n
        row1.append(b) # skapar lista av alla a_n
        
        dlist=[0]*n # skapar lista med n nollor
    for k in row1:
        d=(row1[k+1]-4**-k*row1[k])/1-4**-k # tar två på varandra följande element med början från k ur row1 och definirerar et nytt d     
        dlist[n:]=[] # tar bort sista elementet ur dlist
        dlist2=[d] # ny lista med elementet d
        dlist=dlist2+dlist # lägger dlist2 till dlist
        dlist3.append(dlist) # skapar en ny lista med alla dlist-listor
        
    return (x-1)/dlist3[n] # här vet jag inte hur jag ska hitta rätt element