from sympy.abc import x
from sympy import diff, pprint

f = x**3 + 2*x**2 - 4*x + 1
df1 = diff(f, x)
df2 = diff(f, x, x)
df3 = diff(f, x, x, x)
df4 = diff(f, x, x, x, x)
df5 = diff(f, x, x, x, x, x)
print("Function")
pprint(f)
print("First derivative")
pprint(df1)
print("Second derivative")
pprint(df2)
print("Third derivative")
pprint(df3)
print("Fourth derivative")
pprint(df4)
print("Fifth derivative")
pprint(df5)
