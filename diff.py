from pwn import *
import sympy
from sympy import *
import math

pi=math.pi
e=math.e

def two_var():
    x, y, z = symbols('x y z')
    f1 = x*(e**(-2*x))-(sin(x)/2)
    pf1x = str(f1.diff(x))
    x=3
    evalx = f1
    print(evalx)
    print(eval(str(pf1x)))
    print(pf1x)

two_var()