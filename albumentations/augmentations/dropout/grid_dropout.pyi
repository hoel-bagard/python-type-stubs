"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Iterable, Tuple
from ...core.transforms_interface import DualTransform

__all__ = ["GridDropout"]
class GridDropout(DualTransform):
    """GridDropout, drops out rectangular regions of an image and the corresponding mask in a grid fashion.

    Args:
        ratio (float): the ratio of the mask holes to the unit_size (same for horizontal and vertical directions).
            Must be between 0 and 1. Default: 0.5.
        unit_size_min (int): minimum size of the grid unit. Must be between 2 and the image shorter edge.
            If 'None', holes_number_x and holes_number_y are used to setup the grid. Default: `None`.
        unit_size_max (int): maximum size of the grid unit. Must be between 2 and the image shorter edge.
            If 'None', holes_number_x and holes_number_y are used to setup the grid. Default: `None`.
        holes_number_x (int): the number of grid units in x direction. Must be between 1 and image width//2.
            If 'None', grid unit width is set as image_width//10. Default: `None`.
        holes_number_y (int): the number of grid units in y direction. Must be between 1 and image height//2.
            If `None`, grid unit height is set equal to the grid unit width or image height, whatever is smaller.
        shift_x (int): offsets of the grid start in x direction from (0,0) coordinate.
            Clipped between 0 and grid unit_width - hole_width. Default: 0.
        shift_y (int): offsets of the grid start in y direction from (0,0) coordinate.
            Clipped between 0 and grid unit height - hole_height. Default: 0.
        random_offset (boolean): weather to offset the grid randomly between 0 and grid unit size - hole size
            If 'True', entered shift_x, shift_y are ignored and set randomly. Default: `False`.
        fill_value (int): value for the dropped pixels. Default = 0
        mask_fill_value (int): value for the dropped pixels in mask.
            If `None`, transformation is not applied to the mask. Default: `None`.

    Targets:
        image, mask

    Image types:
        uint8, float32

    References:
        https://arxiv.org/abs/2001.04086

    """
    def __init__(self, ratio: float = ..., unit_size_min: int = ..., unit_size_max: int = ..., holes_number_x: int = ..., holes_number_y: int = ..., shift_x: int = ..., shift_y: int = ..., random_offset: bool = ..., fill_value: int = ..., mask_fill_value: int = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, holes: Iterable[Tuple[int, int, int, int]] = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, holes: Iterable[Tuple[int, int, int, int]] = ..., **params) -> np.ndarray:
        ...
    
    def get_params_dependent_on_targets(self, params): # -> dict[str, list[Unknown]]:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['ratio'], Literal['unit_size_min'], Literal['unit_size_max'], Literal['holes_number_x'], Literal['holes_number_y'], Literal['shift_x'], Literal['shift_y'], Literal['random_offset'], Literal['fill_value'], Literal['mask_fill_value']]:
        ...
    


