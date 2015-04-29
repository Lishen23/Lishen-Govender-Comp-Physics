# note this is problem 1 from lecture notes 5 (tutorial problems 2)


class complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def copy(self):
        return complex(self.r,self.i)
num1 = complex()
	print 'real part of num is ' +repr(num1.r)
	print 'imaginary part of num is ' +repr(num1.i)

  
    def __mul__(self,x1):
        a1=self
     
            a1.r=self.r*x1.r-self.i*x1.i             #these 2 equations complex conjugates the answer
            a1.i=self.r*x1.i+self.i*x1.r
       
      return a1

a1 = complex()
	print 'real part of product of  complex no is ' +repr(a1.r)
	print 'imaginary part of product of  complex no is ' +repr(a1.i)


    def __sub__(self,x2):
        a2=self
 
            a2.r=self.r+x2.r
            a2.i=self.i-x2i
          return a2

a2 = complex()
	print 'real part of difference of  complex no is ' +repr(a2.r)
	print 'imaginary part of difference of  complex no is ' +repr(a2.i)  


    def __div__(self,x3):

        a3=self
     
            a3.r=self.r/x3.r-self.i/x3.i             #these 2 equations complex conjugates the answer
            a3.i=self.r/x3.i+self.i/x3.r
       
      return a3

a3 = complex()
	print 'real part of division of  complex no is ' +repr(a1.r)
	print 'imaginary part of division of  complex no is ' +repr(a1.i)