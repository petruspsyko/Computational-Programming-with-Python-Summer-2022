# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:31:01 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio

A = ones((8,8))
B = zeros((8,8))
 
for k in range(8): # antal kolonner
    n=0
    for r in range(4): # halva antalet rader
        # mult med 1/sqrt(2) och adderar parvis elementen i kolonnerna
        # så vi får medel i de översta raderna
        B[r][k]=A[r+n][k]*(1/sqrt(2))+A[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

for k in range(8):
    n=0
    for r in range(4):
    # mult med -1/sqrt(2) resp. 1/sqrt(2) och adderar 
    # för att få skillnaden i de nedersta raderna
    # r+4 eftersom vi ska fylla nedre halvan
        B[r+4][k]=A[r+n][k]*(-1/sqrt(2))+A[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

#imshow(B,cmap='gray')
