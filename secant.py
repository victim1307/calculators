import math
from pwn import *
pi=math.pi
e=math.e
x0=float(input("x0:"))
x1=float(input("x1:"))
y=input("f(x):")
count=0
print("i |   a    |   b    |   x    |   f(x)  | +/- |")
print("----------------------------------------------")
for i in range(0,10):
    x=x0
    vx0=eval(y)
    x=x1
    vx1=eval(y)
    if(count<10):
        x=(((x0*vx1)-(x1*vx0))/(vx1-vx0))
        ans=eval(y)
        if(ans<0):
            print(f"{i+1:02d}"+"| "+f'{x0:1.4f}'+" | "+f'{x1:1.4f}'+" | "+f'{x:1.4f}'+" | "+f'{ans:1.4f}'+" | -ve |")
            dum = x1
            x0 = dum
            x1=x
        else:
            print(f"{i+1:02d}"+"| "+f'{x0:1.4f}'+" | "+f'{x1:1.4f}'+" | "+f'{x:1.4f}'+" | "+f'{ans:1.4f}'+" | +ve |")
            dum = x1
            x0 = dum
            x1=x

        count= count+1
    else:
        print("No roots")