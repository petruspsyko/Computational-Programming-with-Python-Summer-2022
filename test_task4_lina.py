from numpy import *
from matplotlib.pyplot import *

def fast_approx_ln(x,n):
    a_0 = (1+x)/2                  
    g_0 = sqrt(x)
    
    for i in range(n+1): # +1?             
        a_0 = (a_0+g_0)/2           
        g_0 = sqrt(a_0 + g_0) # här produceras a_0+i, vilket heter a_0
        d=[(1+x)/2,a_0] # a0 är här a_0+i, och det första elementet är d_0,0
        
        for k in range(1,i+1): # innan föregående loop avslutas fortsätter den här
            d_0=(d[1]-(4**-k*d[0]))/(1-4**-k)    
            d[:1]=[] # tar bort det första elementet ur d
            d2=[d_0] # skapar ny lista med bara d_0
            d=d+d2 # skapar ny d 
        
    return (x-1)/d_0