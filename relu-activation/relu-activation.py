import numpy as np

def relu(x):
    x = np.asarray(x, dtype=float)
    return np.asarray(np.maximum(0.0, x))