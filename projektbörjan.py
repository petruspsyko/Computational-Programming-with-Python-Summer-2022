# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:58:33 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio

kvinna=imageio.imread('kvinna.jpg',as_gray=True)
#imshow(kvinna)
W_n=zeros((600,600))

for i in range(300): #halva n = 300
    W_n[i][i*2]=(1/sqrt(2))
    W_n[i][2*i+1]=(1/sqrt(2))
for k in range(300):
    W_n[k+300][k*2]=(-1/sqrt(2))
    W_n[k+300][2*k+1]=(1/sqrt(2))
    
A=dot(W_n,kvinna)

W_m=zeros((478,478))

for i in range(239):
    W_m[i][i*2]=(1/sqrt(2))
    W_m[i][2*i+1]=(1/sqrt(2))
for k in range(239):
    W_m[k+239][k*2]=(-1/sqrt(2))
    W_m[k+239][2*k+1]=(1/sqrt(2))

W_mt=W_m.transpose()

B=dot(A,W_mt)


