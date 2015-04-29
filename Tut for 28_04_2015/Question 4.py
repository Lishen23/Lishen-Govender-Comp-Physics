#google not so helpful for this problem, most of what I could find 
#(mainly on stack overflow) suggests to use things within scipy, are 
#we allowed to use funcions from scipy for the scope of this course? 
#lots of the things including the ODEs and PDEs look much easier with scipy

#link below suggests the zeros in the array will fix the dft wrap problem
#http://stackoverflow.com/questions/18384054/what-are-the-downsides-of-convolution-by-fft-compared-to-realspace-convolution

import numpy as np
from matplotlib import pyplot as plt

def conv(x,y):
    x1=np.zeros(x.size) 
    x1[0:x.size]=x  #added zeros

    y1=np.zeros(y.size)
    y1[0:y.size]=y #added zeros
    x1ft=np.fft(x1)
    y1ft=np.fft(y1)
    vect1=np.real(np.ifft(x1ft*y1ft))
    return vect1[0:x.size]


x=np.arange(-10,10,0.1)
sig=4
y=np.exp(-0.5*x**2/sig**2)
y=y/y.sum()

convy=conv(y,y)
plt.plot(x,y)
plt.plot(x,convy)


    
