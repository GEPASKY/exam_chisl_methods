import numpy as np


def f(x):
    return (x - 3) * 2 + x * 2 * np.cos(2 * x)


print(round(f(2.466), 16))
