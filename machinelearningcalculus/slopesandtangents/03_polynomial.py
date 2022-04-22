import numpy as np

def f(x):
    return x**3 + 2*x + 1

epsilon = np.finfo(np.float32).eps
for x in [2, 0, -2]:
    slope = (f(x+epsilon) - f(x))/epsilon
    y = f(x)
    c = y - slope * x
    print("Slope at x={} is {}".format(x, slope))
    print("Tangent line is y={:f}x{:+f}".format(slope,c))
