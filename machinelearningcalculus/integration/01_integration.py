from sympy import integrate, pprint
from sympy.abc import x
import numpy as np

f = 3 * x**2
result = integrate(f, x)
print("Antiderivative of")
pprint(f)
print("is")
pprint(result)
print()

result = integrate(f, (x, 2, 3))
print("Integration of")
pprint(f)
print("for x=2 to x=3 is")
pprint(result)
print()

dx = 0.001
x = np.arange(2, 3, dx)
y = 3 * x**2
result = (y * dx).sum()
print("Numerically using left sum:", result)
x = np.arange(2, 3, dx) + dx
y = 3 * x**2
result = (y * dx).sum()
print("Numerically using right sum:", result)
x = np.arange(2, 3, dx) + dx/2
y = 3 * x**2
result = (y * dx).sum()
print("Numerically using midpoint sum:", result)
