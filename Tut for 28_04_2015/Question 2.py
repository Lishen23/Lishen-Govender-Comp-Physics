
import numpy as np
from matplotlib import pyplot as plt

def cor(f,g):
 
    xft=np.fft(f)
    yft=np.fft(g)
    conyft=np.conj(yft)
    return np.real(np.ifft(xft*conyft))


f=np.arange(-10,10,0.1)
sig=4
g=np.exp(-0.5*f**2/sig**2)
        
gcor=cor(g,g)
plt.plot(f,gcor)
plt.show()
        



