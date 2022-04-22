from sympy.abc import x, y
from sympy import diff, pprint

f2 = x**2 + y**2
df2dx = diff(f2, x)
df2dy = diff(f2, y)
print("Partial derivative of")
pprint(f2)
print("with respect to x is")
pprint(df2dx)
print("and with respect to y is")
pprint(df2dy)
print("gradient at (1,1) is ({},{})".format(df2dx.subs([(x,1),(y,1)]), df2dy.subs([(x,1),(y,1)])))
print("gradient at (2,1) is ({},{})".format(df2dx.subs([(x,2),(y,1)]), df2dy.subs([(x,2),(y,1)])))
