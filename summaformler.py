# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 17:16:40 2022
@author: petrusisaksson
"""
from numpy import *
from matplotlib.pyplot import *

"För summa"

k=0
for i in range(3):
    k=k+i # vi får ett nytt k definierat i loopen för varje iteration
    # första gången är i=0 och k blir då också 0, men andra gången får vi i=1 och alltså k=1

"Ej för summa"

s=0
for i in range(4):
    s=s+1 # här går i över 0,1,2,3 men eftersom i inte finns i ekvationen kommer den bara upprepas fyra gånger
    # det ger oss alltså 4, eftersom s=0. jämför med nästa
    
"För summa"

r=0
for i in range(5):
    r=r+i+1 # ger oss summan av x+1 då x går från 0 till 4
print(r)