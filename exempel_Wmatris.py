# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:53:00 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio

"Exempel för att skapa Wavelet transformation"

glass=iio.imread('glass.jpg',as_gray=True)

def Wavelet_trans(A):
        n=[A.shape][0][0]
        W_n=zeros((n,n))
        r=int(n/2)
        m=[A.shape][0][1]
        W_m=zeros((m,m))
        p=int(m/2)
        wf=1/sqrt(2)
    
        for i in range(r):    
            W_n[i][i*2]=W_n[i][2*i+1]=W_n[i+r][2*i+1]=wf
            W_n[i+r][i*2]=-wf
    
            for k in range(p):
                W_m[k][k*2]=W_m[k][2*k+1]=W_m[k+p][2*k+1]=wf
                W_m[k+p][k*2]=-wf
    
        return matmul((matmul(W_n,A)),W_m.transpose())

iio.imsave('glass.jpg',glass)
