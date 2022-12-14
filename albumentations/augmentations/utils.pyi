"""
This type stub file was generated by pyright.
"""

from typing import Callable, Union

import numpy as np
from albumentations.core.transforms_interface import KeypointInternalType
from typing_extensions import Concatenate, ParamSpec


__all__ = ["read_bgr_image", "read_rgb_image", "MAX_VALUES_BY_DTYPE", "NPDTYPE_TO_OPENCV_DTYPE", "clipped", "get_opencv_dtype_from_numpy", "angle_2pi_range", "clip", "preserve_shape", "preserve_channel_dim", "ensure_contiguous", "is_rgb_image", "is_grayscale_image", "is_multispectral_image", "get_num_channels", "non_rgb_warning", "_maybe_process_in_chunks"]
P = ParamSpec("P")
MAX_VALUES_BY_DTYPE = ...
NPDTYPE_TO_OPENCV_DTYPE = ...
def read_bgr_image(path): # -> NDArray[uint8]:
    ...

def read_rgb_image(path): # -> NDArray[uint8]:
    ...

def clipped(func: Callable[Concatenate[np.ndarray, P], np.ndarray]) -> Callable[Concatenate[np.ndarray, P], np.ndarray]:
    ...

def clip(img: np.ndarray, dtype: np.dtype, maxval: float) -> np.ndarray:
    ...

def get_opencv_dtype_from_numpy(value: Union[np.ndarray, int, np.dtype, object]) -> int:
    """
    Return a corresponding OpenCV dtype for a numpy's dtype
    :param value: Input dtype of numpy array
    :return: Corresponding dtype for OpenCV
    """
    ...

def angle_2pi_range(func: Callable[Concatenate[KeypointInternalType, P], KeypointInternalType]) -> Callable[Concatenate[KeypointInternalType, P], KeypointInternalType]:
    ...

def preserve_shape(func: Callable[Concatenate[np.ndarray, P], np.ndarray]) -> Callable[Concatenate[np.ndarray, P], np.ndarray]:
    """Preserve shape of the image"""
    ...

def preserve_channel_dim(func: Callable[Concatenate[np.ndarray, P], np.ndarray]) -> Callable[Concatenate[np.ndarray, P], np.ndarray]:
    """Preserve dummy channel dim."""
    ...

def ensure_contiguous(func: Callable[Concatenate[np.ndarray, P], np.ndarray]) -> Callable[Concatenate[np.ndarray, P], np.ndarray]:
    """Ensure that input img is contiguous."""
    ...

def is_rgb_image(image: np.ndarray) -> bool:
    ...

def is_grayscale_image(image: np.ndarray) -> bool:
    ...

def is_multispectral_image(image: np.ndarray) -> bool:
    ...

def get_num_channels(image: np.ndarray) -> int:
    ...

def non_rgb_warning(image: np.ndarray) -> None:
    ...

