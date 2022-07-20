# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:53:00 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Exempel för att skapa W-matris"

n=4

W=zeros((n,n))

for i in range(2): #halva n
    W[i][i*2]=(1/sqrt(2))
    W[i][2*i+1]=(1/sqrt(2))
for k in range(2): #halva n
    W[k+2][k*2]=(-1/sqrt(2)) #k + halva n
    W[k+2][2*k+1]=(1/sqrt(2)) #k + halva n
        

