from sympy.abc import x, y
from sympy import diff, sqrt, pprint

f = x**2 - 10
g = sqrt(f)
result = diff(g, x)
print("Function")
pprint(g)
print("has derivative")
pprint(result)
