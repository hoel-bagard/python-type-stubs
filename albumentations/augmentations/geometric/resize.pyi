"""
This type stub file was generated by pyright.
"""

from typing import Dict, Sequence, Tuple, Union

import numpy as np

from ...core.transforms_interface import BoxInternalType, DualTransform, KeypointInternalType

__all__ = ["RandomScale", "LongestMaxSize", "SmallestMaxSize", "Resize"]
class RandomScale(DualTransform):
    """Randomly resize the input. Output image size is different from the input image size.

    Args:
        scale_limit ((float, float) or float): scaling factor range. If scale_limit is a single float value, the
            range will be (-scale_limit, scale_limit). Note that the scale_limit will be biased by 1.
            If scale_limit is a tuple, like (low, high), sampling will be done from the range (1 + low, 1 + high).
            Default: (-0.1, 0.1).
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def __init__(self, scale_limit=..., interpolation=..., always_apply=..., p=...) -> None:
        ...
    
    def get_params(self): # -> dict[str, float]:
        ...
    
    def apply(self, img, scale=..., interpolation=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_bbox(self, bbox, **params): # -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint, scale=..., **params): # -> KeypointInternalType:
        ...
    
    def get_transform_init_args(self): # -> dict[str, Any | Unknown | tuple[Unknown, ...] | tuple[int | float, ...]]:
        ...
    


class LongestMaxSize(DualTransform):
    """Rescale an image so that maximum side is equal to max_size, keeping the aspect ratio of the initial image.

    Args:
        max_size (int, list of int): maximum size of the image after the transformation. When using a list, max size
            will be randomly selected from the values in the list.
        interpolation (OpenCV flag): interpolation method. Default: cv2.INTER_LINEAR.
        p (float): probability of applying the transform. Default: 1.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def __init__(self, max_size: Union[int, Sequence[int]] = ..., interpolation: int = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, max_size: int = ..., interpolation: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, max_size: int = ..., **params) -> KeypointInternalType:
        ...
    
    def get_params(self) -> Dict[str, int]:
        ...
    
    def get_transform_init_args_names(self) -> Tuple[str, ...]:
        ...
    


class SmallestMaxSize(DualTransform):
    """Rescale an image so that minimum side is equal to max_size, keeping the aspect ratio of the initial image.

    Args:
        max_size (int, list of int): maximum size of smallest side of the image after the transformation. When using a
            list, max size will be randomly selected from the values in the list.
        interpolation (OpenCV flag): interpolation method. Default: cv2.INTER_LINEAR.
        p (float): probability of applying the transform. Default: 1.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def __init__(self, max_size: Union[int, Sequence[int]] = ..., interpolation: int = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, max_size: int = ..., interpolation: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, max_size: int = ..., **params) -> KeypointInternalType:
        ...
    
    def get_params(self) -> Dict[str, int]:
        ...
    
    def get_transform_init_args_names(self) -> Tuple[str, ...]:
        ...
    


class Resize(DualTransform):
    """Resize the input to the given height and width.

    Args:
        height (int): desired height of the output.
        width (int): desired width of the output.
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        p (float): probability of applying the transform. Default: 1.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def __init__(self, height, width, interpolation=..., always_apply=..., p=...) -> None:
        ...
    
    def apply(self, img, interpolation=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_bbox(self, bbox, **params): # -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint, **params): # -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['height'], Literal['width'], Literal['interpolation']]:
        ...
    


