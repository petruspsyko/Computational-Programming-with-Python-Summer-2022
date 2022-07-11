from numpy import *
from matplotlib.pyplot import *

#1
def approx_ln(x, n):                #this function will approximate the logarithm by n steps
    
    a_0 = (1+x)/2                   #the values that are given
    g_0 = sqrt(x)
    
    for i in range(n):              #as long as i is in range n, we have the following function
        a_0 = (a_0+g_0)/2           #we put the values a_0 and g_0 in the already given formula
        g_0 = sqrt(a_0 + g_0)
    return (x-1)/a_0                #we get a value after n iterations on a_0

#2
#Plot both functions, ln and approx_ln, in one plot. Do this for different values of n.
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
    y.append(approx_ln(i,5))                        #to see what happens to the function if the value of n is different we change it to 5

axis.plot(x,y, color="red", label='approx_ln, n=5')
legend()
show()

#2.1
#Plot the difference of both functions in another plot. Do this for different values of n.

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
#Consider x = 1.41. Plot the absolut value of the error versus n.
figure3, axis2=subplots()

def error_func(x):
    return abs(log(1.41)-approx_ln(1.41,x))

x = range(2, 100)
y = []
for i in x:
    y.append(error_func(i))

axis2.plot(x,y, color="green")