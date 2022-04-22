from sympy.abc import x, y
from sympy import diff, pprint

f = x**2 + 3*x*y + 4*y**2
fx = diff(f, x)
fy = diff(f, y)
fxx = diff(fx, x)
fyy = diff(fy, y)
fxy = diff(fx, y)
fyx = diff(fy, x)
print("Function")
pprint(f)
print("f_x =")
pprint(fx)
print("f_y =")
pprint(fy)
print("f_xx =")
pprint(fxx)
print("f_yy =")
pprint(fyy)
print("f_xy =")
pprint(fxy)
print("f_yx =")
pprint(fyx)
