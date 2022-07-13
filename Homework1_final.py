from numpy import *
from matplotlib.pyplot import *

"""
Created on Thu Jul  7 11:02:55 2022
@author: Anhelina Lysobyk & Petrus Isaksson
"""

#1
def approx_ln(x, n):                #this function will approximate the logarithm by n steps
    
    a_0 = (1+x)/2                   #the values that are given
    g_0 = sqrt(x)
    
    for i in range(n):              #as long as i is in range n, we have the following function
        a_0 = (a_0+g_0)/2           #we put the values a_0 and g_0 in the already given formula
        g_0 = sqrt(a_0 * g_0)
    return (x-1)/a_0                #we get a value after n iterations on a_0

#2
figure1, axis=subplots()
x = range(1, 101)                                   #the value of x is somewhere in the range of 1 to 100
y = log(x)                                          #y=ln(x)

axis.plot(x,y, color="blue", label='y=ln(x)')            #plot the function y=ln(x) and add a tittle
legend()
show()

x = range(1,101)                                      
y = []
for i in x:
    y.append(approx_ln(i,1))                        #here we plot our function approx_ln by appending it to the y axis

axis.plot(x,y, color="green", label='approx_ln, n=1')
legend()
show()

x = range(1,101)
y = []
for i in x:
    y.append(approx_ln(i,2))                        #to see what happens to the function if the value of n is different we change it to 5

axis.plot(x,y, color="red", label='approx_ln, n=5')
legend()
show()

#2.1
def difference(x,n):
    return log(x) - approx_ln(x, n)

figure2, axis1 = subplots()
x = range(1,101)
y = []
for i in x:
    y.append(difference(i,1))                        #n=1, 1 iteration

axis1.plot(x,y, color="blue", label='difference function, n=1')
legend()
show()

x = range(1,101)
y = []
for i in x:
    y.append(difference(i,5))                        #n=5

axis1.plot(x,y, color="green", label='difference function, n=5')
legend()
show()

#3
figure3, axis2=subplots()

def error_func(x):
    return abs(log(1.41)-approx_ln(1.41,x))

x = range(1, 100)
y = []
for i in x:
    y.append(error_func(i))

axis2.plot(x,y, color="green")

#4
def fast_approx_ln(x,n):
    a_0 = (1+x)/2                  
    g_0 = sqrt(x)
    A=zeros([n,n]) # skapar n*n-matris med nollor
    A[0,0]=a_0 # stoppar in a_0 på första platsen (k,i)
    
    for i in range(1,n): # vi hoppar över element(0,0)           
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 * g_0) # här produceras a_0+i, vilket heter a_0
        A[0,i]=a_0 # lägg till a_i på plats i 
        
    for i in range(1,n):
        
        for k in range(1,n):
            A[i,k]=(A[k-1,i]-((4**-k)*A[k-1,i-1]))/(1-(4**-k))
            
    return (x-1)/A[n-1,n-1]

#5
#x = arange(-50.0, 50.0, 0.1)
#y = arange(0,100.0, 0.1)

figure4,axis3=subplots()

x = range(1,100) #2 iterations
y = []
for i in x:
    y.append(fast_approx_ln(i, 2))

axis3.plot(x,y, color="blue")
yscale('log')
show()

x = range(1,100) #3 iterations
y = []
for i in x:
    y.append(fast_approx_ln(i, 3))

axis3.plot(x,y, color="green")
yscale('log')
show()

x = range(1,100) #4 iterations
y = []
for i in x:
    y.append(fast_approx_ln(i, 4))

axis3.plot(x,y, color="red")
yscale('log')
show()

x = range(1,100) #5 iterations
y = []
for i in x:
    y.append(fast_approx_ln(i, 5))

axis3.plot(x,y, color="turquoise")
yscale('log')
show()