import numpy as np

def g(x):
    return 1-x

x = -1
epsilon = np.finfo(float).eps

print("Left limit is", g(x-epsilon))
print("Right limit is", g(x+epsilon))
