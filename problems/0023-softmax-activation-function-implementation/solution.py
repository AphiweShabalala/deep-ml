import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    x = np.asarray(scores, dtype=float)
    exp_shift = np.exp(x - np.max(x, axis=-1, keepdims=True))
    result = exp_shift/np.sum(exp_shift, axis=-1, keepdims = True)
    return result.tolist()
    pass