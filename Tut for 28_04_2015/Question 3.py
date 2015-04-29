import numpy as np
from matplotlib import pyplot as plt
def shift(x,n):
   
    vec1=0*x 
    vec1[n]=1
    vec1fft=np.fft(vec1)
    xft=np.fft(x)
    return np.real(np.ifft(xft*vec1fft))



def cor(x,y): # will change f and g back to x and y so things make sense
 
    xft=np.fft(x)
    yft=np.fft(y)
    conyft=np.conj(yft)
    return np.real(np.ifft(xft*conyft))


x=np.arange(-10,10,0.1)
sig=4
y=np.exp(-0.5*x**2/sig**2) #gaussian
        
ycor=cor(y,y)
shift1=shift(y,y.size/2) #we use y.size to get the length of the array and shift by half of it


plt.plot(x,ycor)
plt.plot(x,shift1)        
plt.show()
        

