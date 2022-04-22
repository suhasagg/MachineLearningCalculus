from sympy import limit, sin, pprint
from sympy.abc import x

expression = x**2 * sin(1/x)
result = limit(expression, x, 0)
print("Limit of")
pprint(expression)
print("at x=0 is", result)
