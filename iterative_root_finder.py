import math
from pwn import *
a=float(input("a:"))
b=float(input("b:"))
y=input("f(x):")
#x**2+3*x+2
print("i |   a    |   b    |   x    | +/- |")
print("------------------------------------")
for i in range(0,5):
    x=(a+b)/2
    if(eval(y)<0):
        print(f"{i+1:02d}"+"| "+f'{a:1.4f}'+" | "+f'{b:1.4f}'+" | "+f'{x:1.4f}'+" | -ve |")
        b=x
    else:
        print(f"{i+1:02d}"+"| "+f'{a:1.4f}'+" | "+f'{b:1.4f}'+" | "+f'{x:1.4f}'+" | +ve |")
        a=x