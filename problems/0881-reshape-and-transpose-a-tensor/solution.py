import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    pass
    flat = x.reshape(-1)
    rearranged = flat.reshape(new_shape)
    return rearranged

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    pass
    Transposed = torch.transpose(x, -2, -1)
    return  Transposed
