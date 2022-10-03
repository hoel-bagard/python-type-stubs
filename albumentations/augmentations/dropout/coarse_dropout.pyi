"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Iterable, List, Optional, Sequence, Tuple, Union
from ...core.transforms_interface import DualTransform, KeypointType

__all__ = ["CoarseDropout"]
class CoarseDropout(DualTransform):
    """CoarseDropout of the rectangular regions in the image.

    Args:
        max_holes (int): Maximum number of regions to zero out.
        max_height (int, float): Maximum height of the hole.
        If float, it is calculated as a fraction of the image height.
        max_width (int, float): Maximum width of the hole.
        If float, it is calculated as a fraction of the image width.
        min_holes (int): Minimum number of regions to zero out. If `None`,
            `min_holes` is be set to `max_holes`. Default: `None`.
        min_height (int, float): Minimum height of the hole. Default: None. If `None`,
            `min_height` is set to `max_height`. Default: `None`.
            If float, it is calculated as a fraction of the image height.
        min_width (int, float): Minimum width of the hole. If `None`, `min_height` is
            set to `max_width`. Default: `None`.
            If float, it is calculated as a fraction of the image width.

        fill_value (int, float, list of int, list of float): value for dropped pixels.
        mask_fill_value (int, float, list of int, list of float): fill value for dropped pixels
            in mask. If `None` - mask is not affected. Default: `None`.

    Targets:
        image, mask, keypoints

    Image types:
        uint8, float32

    Reference:
    |  https://arxiv.org/abs/1708.04552
    |  https://github.com/uoguelph-mlrg/Cutout/blob/master/util/cutout.py
    |  https://github.com/aleju/imgaug/blob/master/imgaug/augmenters/arithmetic.py
    """
    def __init__(self, max_holes: int = ..., max_height: int = ..., max_width: int = ..., min_holes: Optional[int] = ..., min_height: Optional[int] = ..., min_width: Optional[int] = ..., fill_value: int = ..., mask_fill_value: Optional[int] = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def check_range(self, dimension): # -> None:
        ...
    
    def apply(self, img: np.ndarray, fill_value: Union[int, float] = ..., holes: Iterable[Tuple[int, int, int, int]] = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, mask_fill_value: Union[int, float] = ..., holes: Iterable[Tuple[int, int, int, int]] = ..., **params) -> np.ndarray:
        ...
    
    def get_params_dependent_on_targets(self, params): # -> dict[str, list[Unknown]]:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def apply_to_keypoints(self, keypoints: Sequence[KeypointType], holes: Iterable[Tuple[int, int, int, int]] = ..., **params) -> List[KeypointType]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['max_holes'], Literal['max_height'], Literal['max_width'], Literal['min_holes'], Literal['min_height'], Literal['min_width'], Literal['fill_value'], Literal['mask_fill_value']]:
        ...
    


