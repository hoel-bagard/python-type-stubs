"""
This type stub file was generated by pyright.
"""

from typing import Iterable, Tuple, Union

import numpy as np
from albumentations.augmentations.utils import preserve_shape


__all__ = ["cutout", "channel_dropout"]
@preserve_shape
def channel_dropout(img: np.ndarray, channels_to_drop: Union[int, Tuple[int, ...], np.ndarray], fill_value: Union[int, float] = ...) -> np.ndarray:
    ...

def cutout(img: np.ndarray, holes: Iterable[Tuple[int, int, int, int]], fill_value: Union[int, float] = ...) -> np.ndarray:
    ...

