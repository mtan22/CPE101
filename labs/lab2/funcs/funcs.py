#Michelle Tan
#Instructor:Turner
#Section:01

import math
def f(x):
   fValue  = 7*x**2 + 2*x
   return fValue

def g(x,y):
   gValue = ((x**2 + y**2)/(3*x))
   return gValue

def hypotenuse(a,b):
   c2 = a**2 + b**2
   c = math.sqrt(c2)
   return c

def is_positive(x):
   return (x>0)
