import numpy as np

from matplotlib import pyplot as plt

def vector(n):

   #Question 1

    x=np.arange(0,n)

    x=0.5*x*np.pi/(n)
    return x

def intcos(n):
    dx=np.pi/2/n
    vector1=vector(n)
    sumcos=np.sum(np.cos(vector1))
    return dx*tot

def intcos_simp(n):

    dx=np.pi/2/(n)*2

    #Question 3

    vector1=np.cos(vector(n))
    even=vector1[2:-1:2]
    odd=vector1[1:-1:2]
    sumcos=np.sum(even)/3+np.sum(odd)*2/3+vector1[0]/6+vector1[-1]/6
    return sumcos*dx

if __name__=='__main__':
    
    print 'Question 2'
    npoints=[10,30,100,300,1000]    
    for n in npoints:
        ans1=intcos(n)
        print 'The integral with ' + repr(n) + ' points has answer ' + repr(ans1)


    print 'Question 4'
    value=intcos_simp(11)
    e1=np.abs(value-
    print 'error on 11 points is ' + repr(value)
    for n in npoints:
        =np.abs(intcos_simp(n)-1)
        print 'The simpsons error for ' + repr(n) + ' points is ' + repr(e1)


    print 'Question 5'
   


    
