# Program      : Euler's method
# Author       : MOOC team Mathematical Modelling Basics
# Created      : April, 2017

import numpy as np
import matplotlib.pyplot as plt

def fish_predict(Dt):    
    t_init = 0
    t_end = 30
    P_init = 30 
    n_steps = int(round((t_end-t_init)/Dt)) 


    t_arr = np.zeros(n_steps + 1)           
    P_arr = np.zeros(n_steps + 1)           
    t_arr[0] = t_init                       
    P_arr[0] = P_init                       

    # Euler's method

    for i in range (1, n_steps + 1):
        P = P_arr[i-1]
        t = t_arr[i-1]
        dPdt = 0.7*P*(1-P/750)-20                        
        P_arr[i] = P + Dt*dPdt              
        t_arr[i] = t + Dt                   

    return P_arr,t_arr
# Plot the results

p1,t1 = fish_predict(1)
p2,t2 = fish_predict(0.5)
p3,t3 = fish_predict(0.25)


fig = plt.figure()                      
plt.plot(t1, p1, linewidth = 4)   
plt.plot(t2, p2, linewidth = 4)
plt.plot(t3, p3, linewidth = 4)
#plt.plot([13,13],[0,750],'r',linewidth=2)

plt.title('fish', fontsize = 25)  
plt.xlabel('t', fontsize = 20)
plt.ylabel('P(t)', fontsize = 20)
plt.legend(['Dt = 1','Dt = 0.5','Dt = 0.25'])

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.grid(True)                          
plt.axis([0, 25, 0, 800])                

plt.show()                              

# save the figure as .jpg
#fig.savefig('Rainbowfish.png', dpi=fig.dpi, bbox_inches = "tight")