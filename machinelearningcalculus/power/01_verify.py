from sympy import diff, pprint
from sympy.abc import x

expressions = [x**2, 3*x**5, 4*x**9]
for expression in expressions:
    result = diff(expression, x)
    print("Derivative of")
    pprint(expression)
    print("with respect to x is")
    pprint(result)
    print()
