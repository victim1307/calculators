import math
from pwn import *
x0=float(input("x0:"))
x1=float(input("x1:"))
y=input("f(x):")
#x**2+3*x+2
print("i |   a    |   b    |   x    |   f(x)  | +/- |")
print("----------------------------------------------")
for i in range(0,10):
    x=x0
    vx0=eval(y)
    x=x1
    vx1=eval(y)
    if(vx1*vx0<0):
        x=(((x0*vx1)-(x1*vx0))/(vx1-vx0))
        ans=eval(y)
        if(ans<0):
            print(f"{i+1:02d}"+"| "+f'{x0:1.4f}'+" | "+f'{x1:1.4f}'+" | "+f'{x:1.4f}'+" | "+f'{ans:1.4f}'+" | -ve |")
            x0=x
        else:
            print(f"{i+1:02d}"+"| "+f'{x0:1.4f}'+" | "+f'{x1:1.4f}'+" | "+f'{x:1.4f}'+" | "+f'{ans:1.4f}'+" | +ve |")
            x1=x
    else:
        print("No roots")