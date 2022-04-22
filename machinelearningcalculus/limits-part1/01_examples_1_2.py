from sympy import limit, oo, ln, simplify, pprint
from sympy.abc import x

expression = ln(x-1)/(x-2)
result = limit(expression, x, 2)
print("Limit of")
pprint(expression)
print("at x = 2 is", result)
print()

expression = ln(x)/x
result = limit(expression, x, oo)
print("Limit of")
pprint(expression)
print("at x = infinity is", result)
