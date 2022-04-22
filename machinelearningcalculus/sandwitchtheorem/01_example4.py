from sympy import limit, sqrt, pprint
from sympy.abc import x

expression = sqrt(x+1)
result = limit(expression, x, -1)
print("Limit of")
pprint(expression)
print("at x=-1 is", result)
