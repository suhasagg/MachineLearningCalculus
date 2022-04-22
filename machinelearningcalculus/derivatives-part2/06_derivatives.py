# finding the derivative of the sine and cosine functions
from sympy import diff
from sympy import sin
from sympy import cos
from sympy import symbols

# define variable as symbol
x = symbols('x')

# find the first derivative of sine and cosine with respect to x
print('The first derivative of sine is:', diff(sin(x), x))
print('The first derivative of cosine is:', diff(cos(x), x))

# find the second derivative of sine and cosine with respect to x
print('\nThe second derivative of sine is:', diff(sin(x), x, x))
print('The second derivative of cosine is:', diff(cos(x), x, x))

# find the second derivative of sine and cosine with respect to x
print('\nThe second derivative of sine is:', diff(sin(x), x, 2))
print('The second derivative of cosine is:', diff(cos(x), x, 2))
