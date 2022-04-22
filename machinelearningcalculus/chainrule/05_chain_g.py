from sympy.abc import x, y
from sympy import diff, cos, exp, pprint

r = x*cos(y)
s = x*exp(y)
t = x + y
h = r**2 - r*s + t**3
dhdx = diff(h, x)
dhdy = diff(h, y)
print("Function")
pprint(h)
print("Derivative with respect to x")
pprint(dhdx)
print("Derivative with respect to y")
pprint(dhdy)
