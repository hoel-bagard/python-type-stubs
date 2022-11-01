"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Tuple, Union

import numpy as np
from albumentations.core.transforms_interface import ImageOnlyTransform

__all__ = ["Cutout"]
class Cutout(ImageOnlyTransform):
    """CoarseDropout of the square regions in the image.

    Args:
        num_holes (int): number of regions to zero out
        max_h_size (int): maximum height of the hole
        max_w_size (int): maximum width of the hole
        fill_value (int, float, list of int, list of float): value for dropped pixels.

    Targets:
        image

    Image types:
        uint8, float32

    Reference:
    |  https://arxiv.org/abs/1708.04552
    |  https://github.com/uoguelph-mlrg/Cutout/blob/master/util/cutout.py
    |  https://github.com/aleju/imgaug/blob/master/imgaug/augmenters/arithmetic.py
    """
    def __init__(self, num_holes: int = ..., max_h_size: int = ..., max_w_size: int = ..., fill_value: Union[int, float] = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, fill_value: Union[int, float] = ..., holes=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def get_params_dependent_on_targets(self, params: Dict[str, Any]) -> Dict[str, Any]:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_transform_init_args_names(self) -> Tuple[str, ...]:
        ...
    


