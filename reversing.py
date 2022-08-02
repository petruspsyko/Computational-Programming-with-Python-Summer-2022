# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:51:21 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *
import imageio as iio

#Download the image to be reversed
kvinna1 = iio.imread('kvinna1.jpg',as_gray=True)
kvinna = iio.imread('kvinna.jpg',as_gray=True)

#Function to trim the picture (trim) - get rid of odd rows/columns
def trim (data):
    N, M = data.shape
    if N % 2 != 0:
        data=data[0:N-1,:]
    if M % 2 != 0:
        data=data[:,0:M-1]
    return (data)

#Trim image size
N,M = trim(kvinna1).shape

#Function (Create Matrix)
def createMatrix (k):
    A = 1/sqrt(2)
    n = int(k/2)
    W = np.zeros((n*2,n*2))

    for i in range (n):
        W[i, 2*i] = A
        W[i, 2*i+1] = A
        W[i+n, 2*i] = -A
        W[i+n, 2*i+1] = A     
    
    return (W)

W_n = createMatrix (int(N))
W_m = createMatrix (int(M))
W_nt=W_n.transpose()

imshow(matmul(matmul(W_nt,kvinna1),W_m),cmap='gray')
#print(matmul(matmul(W_nt,kvinna1),W_m))
