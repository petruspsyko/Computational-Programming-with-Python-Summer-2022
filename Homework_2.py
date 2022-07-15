# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:49:17 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"  

class Interval:
    def __init__(self,real_left,real_right=None): #we have set a default value for real_right 
        if isinstance(real_left,complex):
            raise TypeError("Wrong type!")
        elif isinstance(real_right,complex):
            raise TypeError("Wrong type!")
        elif real_right is not None and real_left > real_right != 0:#the last part is for making possible [0,0]
            raise TypeError("Not an interval!")
        self.real_left=real_left
        self.real_right=real_right if real_right is not None else real_left
    
    "Task 2"
    #addition
    def __add__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(L1+other,R1+other)
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(L1+L2,R1+R2)
    
    def __radd__(self, other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(L1+other,R1+other)
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(L2+L1,R2+R1)

    def __repr__(self):
        return f'[{self.real_left},{self.real_right}]'
    #subtraction
    def __sub__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(L1-other,R1-other)
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(L1-R2,R1-L2)
        
    def __rsub__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(other-R1,other-L1)
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(L2-R1,R2-L1)
    #multiplication
    def __mul__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(min([L1*other,R1*other]),max([L1*other,R1*other]))
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(min([L1*L2,L1*R2,R1*L2,R1*R2]),max([L1*L2,L1*R2,R1*L2,R1*R2]))
    
    def __rmul__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other,int) or isinstance(other,float):
            return Interval(min([other*L1,other*R1]),max([other*L1,other*R1]))
        else:
            L2,R2=other.real_left,other.real_right
            return Interval(min([L1*L2,L1*R2,R1*L2,R1*R2]),max([L1*L2,L1*R2,R1*L2,R1*R2]))
    
    #division
    def __truediv__(self,other):
        L1,R1=self.real_left,self.real_right
        if isinstance(other, Interval):
            L2,R2=other.real_left,other.real_right
            if L2==0 or R2==0:
                raise TypeError("It's not possible to divide by an interval containing zero!")
            #elif min([L1/L2,L1/R2,R1/L2,R1/R2]) - max([L1/L2,L1/R2,R1/L2,R1/R2]) <= -10**100:
                #raise TypeError("The result is an infinitely large interval :)") #ska vi ta bort den här? den verkar inte funka nu, eller? enligt claus behövdes inget mer än att förbjuda att dela med 0.
            else:
                return Interval(min([L1/L2,L1/R2,R1/L2,R1/R2]),max([L1/L2,L1/R2,R1/L2,R1/R2]))        
    
    "Task 5"
    
    def __contains__(self,item):
        if self.real_left <= item <= self.real_right:
            return True
        else:
            return False
  
    def __neg__(self):
        L1,R1=self.real_left,self.real_right
        return Interval(-R1,-L1)

    "Task 9"    

    def __pow__(self,other):
        L1,R1=self.real_left,self.real_right
        if other <= 1:
            raise TypeError("The exponent needs to greater than, or equal to, 1.")
        elif other%2 != 0:
                if isinstance(other,int) or isinstance(other,float):
                    return Interval(L1**other,R1**other)
        else:
            if not L1 < 0:
                return Interval(L1**other,R1**other)
            elif R1 < 0:
                return Interval(R1**other,L1**other)
            else:
                return Interval(0,max(L1**other,R1**other))

    def lowerb(self):
        L1,R1=self.real_left,self.real_right
        return L1 

    def upperb(self):
        L1,R1=self.real_left,self.real_right
        return R1

#x=Interval(-2,3)
#q=Interval(1.0,4.0)
#print(5 in q)
                      
#example run with two intervals
#q=Interval(1.,10.)
#z=Interval(10**-100,4.) 
#print(q/z)   
        
"Task 3"
#Included in task 2. See "__repr__".

"Task 4"

I1=Interval(1,4)
#print(I1)
I2=Interval(-2,-1)
#print(I2)
#print(I1+I2)
#print(I1-I2)
#print(I1*I2)
#print(I1/I2)

"Task 6"
#contained in Task 2

"Task 7"
#See Task 2 under __init__.

"Task 8"
#defined in dunder methods. __neg__ under Task 5.

"Task 10"

upperbv=[]
for xu in linspace(0.,1,1000)+0.5:
    upperbv.append(Interval(0,xu))
lowerbv=[]
for xl in linspace(0.,1,1000):
    lowerbv.append(Interval(xl,1000))
thousandint=[]
for i in range(1000):
    thousandint.append(lowerbv[i]+upperbv[i])
thousandint_final=[]
for k in range(1000):
    thousandint_final.append(thousandint[k]-Interval(1000,0))
    
def f(I):
    return 3*I**3-2*I**2-5*I-1

flist=[]
for I in range(1000):
    flist.append(f(thousandint_final[I]))

#defined method lowerb and method upperb
yl=[]
for i in range(1000):
    yl.append(Interval.lowerb(flist[i]))

yu=[]
for i in range(1000):
    yu.append(Interval.upperb(flist[i]))

figure, axis=subplots()
x=linspace(0.,1,1000)
axis.plot(x,yu,color="green")
x=linspace(0.,1,1000)
axis.plot(x,yl,color="purple")
title('$p(I)=3I^3-2I^2-5I-1,I=Interval(x,x+0.5)$')
xlabel('x')
ylabel('p(I)')
xlim(0,1)
ylim(-10,4)
show()


