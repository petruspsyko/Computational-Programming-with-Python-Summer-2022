# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:58:33 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio

kvinna=iio.imread('kvinna.jpg',as_gray=True)
#imshow(kvinna)
W_n=zeros((600,600))

for i in range(300): #halva n = 600
    W_n[i][i*2]=(1/sqrt(2))
    W_n[i][2*i+1]=(1/sqrt(2))
for k in range(300): #halva n = 600
    W_n[k+300][k*2]=(-1/sqrt(2)) #k + halva n = 600
    W_n[k+300][2*k+1]=(1/sqrt(2)) #k + halva n = 600
    
A=matmul(W_n,kvinna)

W_m=zeros((478,478))

for i in range(239):
    W_m[i][i*2]=(1/sqrt(2))
    W_m[i][2*i+1]=(1/sqrt(2))
for k in range(239):
    W_m[k+239][k*2]=(-1/sqrt(2))
    W_m[k+239][2*k+1]=(1/sqrt(2))

W_mt=W_m.transpose()

B=matmul(A,W_mt)

#imshow(B,cmap='gray')

kvinna2=zeros((300,239)) #nästa bild - submatrix
for i in range(300):
    for k in range(239):
        kvinna2[i][k]=B[i][k]

#imshow(kvinna2,cmap='gray')

#Vi börjar om igen.

W2_n=zeros((300,300))

for i in range(150): #halva n = 300
    W2_n[i][i*2]=(1/sqrt(2))
    W2_n[i][2*i+1]=(1/sqrt(2))
for k in range(150): #halva n = 300
    W2_n[k+150][k*2]=(-1/sqrt(2)) #som ovan, för W_n
    W2_n[k+150][2*k+1]=(1/sqrt(2))

A2=matmul(W2_n,kvinna2)

#A2 har ett ojämt antal kolonner (239), så vi måste ta bort en

A2_red=A2[:,:238]

W2_m=zeros((238,238))

for i in range(119):
    W2_m[i][i*2]=(1/sqrt(2))
    W2_m[i][2*i+1]=(1/sqrt(2))
for k in range(119):
    W2_m[k+119][k*2]=(-1/sqrt(2))
    W2_m[k+119][2*k+1]=(1/sqrt(2))

W2_mt=W2_m.transpose()

B2=matmul(A2_red,W2_mt)

kvinna3=zeros((150,119)) #nästa bild - submatrix
for i in range(150):
    for k in range(119):
        kvinna3[i][k]=B2[i][k]

imshow(kvinna3,cmap='gray')
