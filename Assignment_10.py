# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:39:36 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"Task 1"

myfile=open('kwh.txt','r')
s=myfile.read() #string
#print(s)
yearmonthday_kwh=s.split() #list
#print(yearmonthday_kwh)
yearmonthday=yearmonthday_kwh[::2] #returns every other element in list
#print(yearmonthday) #list
kwh=yearmonthday_kwh[1::2] #starting with second
#print(kwh) #list 
kwh_data=[]
for element in kwh:
    kwh_data.append(int(element))
#print(kwh_data)

"Task 2"

yearmonthday.reverse()
#print(yearmonthday)
kwh_data.reverse()
#print(kwh_data)

"Task 3"

kwh_data_array=array(kwh_data)
#print(kwh_data_array)
kwh_consumtion=diff(kwh_data_array)
#print(kwh_consumtion)
    
"Task 4"

fig,ax=subplots(figsize=(25,25))
ax.set(xlim=(0,23),ylim=(1,5000))
ax.plot(yearmonthday[:154],kwh_consumtion,color="green")

"Task 5"

kwh_cons_list = kwh_consumtion.tolist() #gör array till lista
xval_min=kwh_cons_list.index(min(kwh_cons_list)) #hittar index för minimum i kwh_cons_list
xval_max=kwh_cons_list.index(max(kwh_cons_list))
#print(yearmonthday[xval_min])
#print(yearmonthday[xval_max])

"Task 7"

k=0
for i in range(len(kwh_cons_list)):
    k=k+kwh_cons_list[i]
#print(k/(len(kwh_cons_list)))

"Task 8"
print(f"The mean value of the kwh consumtion is {k/(len(kwh_cons_list))}.")
    

    
