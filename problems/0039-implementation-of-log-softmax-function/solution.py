import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	x = np.asarray(scores, dtype=float)

	max_x = np.max(x, axis=-1, keepdims=True)

	log_sum_exp = max_x + np.log(np.sum(np.exp(x - max_x), axis=-1,keepdims=True))

	result = x - log_sum_exp
	return result.tolist()
	pass