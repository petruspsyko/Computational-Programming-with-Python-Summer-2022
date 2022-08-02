# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:41:24 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio
import time

# get the start time
st = time.time()

A = iio.imread('kvinna.jpg',as_gray=True)
 
B = zeros((600,478))

for k in range(478): # antal kolonner
    n=0
    for r in range(300): # halva antalet rader
    # mult med 1/sqrt(2) och adderar parvis elementen i kolonnerna
    # så vi får medel i de översta raderna
        B[r][k]=A[r+n][k]*(1/sqrt(2))+A[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

for k in range(478):
    n=0
    for r in range(300):
    # mult med -1/sqrt(2) resp. 1/sqrt(2) och adderar 
    # för att få skillnaden i de nedersta raderna
    # r+300 eftersom vi ska fylla nedre halvan
        B[r+300][k]=A[r+n][k]*(-1/sqrt(2))+A[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

A2 = B.transpose()

B2 = zeros((478,600)) # omvänt

for k in range(600): # antal kolonner
    n=0
    for r in range(239): # halva antalet rader
    # mult med 1/sqrt(2) och adderar parvis elementen i kolonnerna
    # så vi får medel i de översta raderna
        B2[r][k]=A2[r+n][k]*(1/sqrt(2))+A2[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

for k in range(600):
    n=0
    for r in range(239):
    # mult med -1/sqrt(2) resp. 1/sqrt(2) och adderar 
    # för att få skillnaden i de nedersta raderna
    # r+239 eftersom vi ska fylla nedre halvan
        B2[r+239][k]=A2[r+n][k]*(-1/sqrt(2))+A2[r+n+1][k]*(1/sqrt(2)) 
        n=n+1

B_final = B2.transpose()
print(B_final)
#imshow(B_final,cmap='gray')
    
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')