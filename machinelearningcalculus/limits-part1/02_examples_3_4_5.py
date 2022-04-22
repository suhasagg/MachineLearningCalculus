from sympy import limit, oo, sin, cos, simplify, pprint
from sympy.abc import x

expression = x * sin(1/x)
result = limit(expression, x, oo)
print("Limit of")
pprint(expression)
print("at x = infinity is", result)
print()

expression = 1/(1-cos(x)) - 1/x
result = limit(expression, x, 0)
print("Limit of")
pprint(expression)
print("at x = 0 is", result)
print()

expression = (1+x)**(1/x)
result = limit(expression, x, oo)
print("Limit of")
pprint(expression)
print("at x = infinity is", result)
