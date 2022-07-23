# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:53:00 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio

kvinna=iio.imread('kvinna.jpg',as_gray=True)

def Wavelet_trans(A):
    if isinstance(A,int):
        raise TypeError("Not an image!")
    elif isinstance(A,float):
        raise TypeError("Not an image!")
    elif isinstance(A,complex):
        raise TypeError("Not an image!")
    elif [A.shape][0][0] < 2: # Om A bara har en rad 
        raise TypeError("Not a valid format!") 
    elif [A.shape][0][0] == A.size: # Om A endast består av rader - är 1D
        raise TypeError("Not a valid format!")
    else:
        if [A.shape][0][0]%2 != 0: # Om A:s rader är av ojämt antal
            A=A=A[:[A.shape][0][0]-1,:] # Tar bort en av A:s rader
        if [A.shape][0][1]%2 != 0: # Om A:s kolonner är av ojämt antal
            A=A[:,:[A.shape][0][1]-1] # Tar bort en av A:s kolonner
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
    
    B=matmul((matmul(W_n,A)),W_m.transpose()) # B består av fyra submatriser
    
    B2=zeros((r,p)) # Ny matris för den övre vänstra submatrisen    
    for i in range(r):
        for k in range(p):
                B2[i][k]=B[i][k] # Stoppar det i övre vänstra hörnet i B
    return B2

def simplifyimage(A,n): # Halverar antalet pixlar n gånger
    for i in range(n):
        A=Wavelet_trans(A)
    return A 

#imshow(simplifyimage(kvinna,2),cmap='gray')