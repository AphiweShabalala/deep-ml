import numpy as np
def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	# Your code here
	return np.where(z>0, z, alpha*z)
	pass
