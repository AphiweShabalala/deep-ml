import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here
    probs_clip = np.clip(predicted_probs, epsilon, 1-epsilon)

    if true_labels.ndim == 1:
        num_samples = len(true_labels)
        loss = -np.log(probs_clip[np.arange(num_samples),true_labels])
    else:
        loss = -np.sum(true_labels*np.log(probs_clip), axis=-1)

    return float(np.mean(loss))
    pass