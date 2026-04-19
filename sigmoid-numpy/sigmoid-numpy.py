import numpy as np

def sigmoid(x):
    x = np.asarray(x, dtype=float)  # handles scalar, list, ndarray
    return 1.0 / (1.0 + np.exp(-x))