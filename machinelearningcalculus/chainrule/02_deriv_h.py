from sympy.abc import x, y
from sympy import diff, cos, pprint

u = x**3 - 1
h = cos(u)
result = diff(h, x)
print("Function")
pprint(h)
print("has derivative")
pprint(result)
