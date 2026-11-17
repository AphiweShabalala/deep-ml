import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    ones_vec = np.arange(a.shape[0])*0.0 + 1.0
    return np.dot(a,ones_vec)
    pass
