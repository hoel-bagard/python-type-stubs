"""
This type stub file was generated by pyright.
"""

from enum import Enum
from typing import Optional, Sequence, Tuple, Union

import numpy as np
import skimage.transform

from ...core.transforms_interface import (BoxInternalType, DualTransform, ImageColorType, KeypointInternalType,
                                          ScaleFloatType)


__all__ = ["ShiftScaleRotate", "ElasticTransform", "Perspective", "Affine", "PiecewiseAffine", "VerticalFlip", "HorizontalFlip", "Flip", "Transpose", "OpticalDistortion", "GridDistortion", "PadIfNeeded"]
class ShiftScaleRotate(DualTransform):
    """Randomly apply affine transforms: translate, scale and rotate the input.

    Args:
        shift_limit ((float, float) or float): shift factor range for both height and width. If shift_limit
            is a single float value, the range will be (-shift_limit, shift_limit). Absolute values for lower and
            upper bounds should lie in range [0, 1]. Default: (-0.0625, 0.0625).
        scale_limit ((float, float) or float): scaling factor range. If scale_limit is a single float value, the
            range will be (-scale_limit, scale_limit). Note that the scale_limit will be biased by 1.
            If scale_limit is a tuple, like (low, high), sampling will be done from the range (1 + low, 1 + high).
            Default: (-0.1, 0.1).
        rotate_limit ((int, int) or int): rotation range. If rotate_limit is a single int value, the
            range will be (-rotate_limit, rotate_limit). Default: (-45, 45).
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        border_mode (OpenCV flag): flag that is used to specify the pixel extrapolation method. Should be one of:
            cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, cv2.BORDER_REFLECT_101.
            Default: cv2.BORDER_REFLECT_101
        value (int, float, list of int, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
        mask_value (int, float,
                    list of int,
                    list of float): padding value if border_mode is cv2.BORDER_CONSTANT applied for masks.
        shift_limit_x ((float, float) or float): shift factor range for width. If it is set then this value
            instead of shift_limit will be used for shifting width.  If shift_limit_x is a single float value,
            the range will be (-shift_limit_x, shift_limit_x). Absolute values for lower and upper bounds should lie in
            the range [0, 1]. Default: None.
        shift_limit_y ((float, float) or float): shift factor range for height. If it is set then this value
            instead of shift_limit will be used for shifting height.  If shift_limit_y is a single float value,
            the range will be (-shift_limit_y, shift_limit_y). Absolute values for lower and upper bounds should lie
            in the range [0, 1]. Default: None.
        rotate_method (str): rotation method used for the bounding boxes. Should be one of "largest_box" or "ellipse".
            Default: "largest_box"
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, keypoints

    Image types:
        uint8, float32
    """
    def __init__(self, shift_limit=..., scale_limit=..., rotate_limit=..., interpolation=..., border_mode=..., value=..., mask_value=..., shift_limit_x=..., shift_limit_y=..., rotate_method=..., always_apply=..., p=...) -> None:
        ...
    
    def apply(self, img, angle=..., scale=..., dx=..., dy=..., interpolation=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_mask(self, img, angle=..., scale=..., dx=..., dy=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_keypoint(self, keypoint, angle=..., scale=..., dx=..., dy=..., rows=..., cols=..., **params): # -> KeypointInternalType:
        ...
    
    def get_params(self): # -> dict[str, float]:
        ...
    
    def apply_to_bbox(self, bbox, angle, scale, dx, dy, **params): # -> tuple[Unknown, Unknown, Unknown, Unknown]:
        ...
    
    def get_transform_init_args(self): # -> dict[str, Unknown | tuple[Unknown, ...] | tuple[int | float, ...] | Any | int | str | None]:
        ...
    


class ElasticTransform(DualTransform):
    """Elastic deformation of images as described in [Simard2003]_ (with modifications).
    Based on https://gist.github.com/ernestum/601cdf56d2b424757de5

    .. [Simard2003] Simard, Steinkraus and Platt, "Best Practices for
         Convolutional Neural Networks applied to Visual Document Analysis", in
         Proc. of the International Conference on Document Analysis and
         Recognition, 2003.

    Args:
        alpha (float):
        sigma (float): Gaussian filter parameter.
        alpha_affine (float): The range will be (-alpha_affine, alpha_affine)
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        border_mode (OpenCV flag): flag that is used to specify the pixel extrapolation method. Should be one of:
            cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, cv2.BORDER_REFLECT_101.
            Default: cv2.BORDER_REFLECT_101
        value (int, float, list of ints, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
        mask_value (int, float,
                    list of ints,
                    list of float): padding value if border_mode is cv2.BORDER_CONSTANT applied for masks.
        approximate (boolean): Whether to smooth displacement map with fixed kernel size.
                               Enabling this option gives ~2X speedup on large images.
        same_dxdy (boolean): Whether to use same random generated shift for x and y.
                             Enabling this option gives ~2X speedup.

    Targets:
        image, mask, bbox

    Image types:
        uint8, float32
    """
    def __init__(self, alpha=..., sigma=..., alpha_affine=..., interpolation=..., border_mode=..., value=..., mask_value=..., always_apply=..., approximate=..., same_dxdy=..., p=...) -> None:
        ...
    
    def apply(self, img, random_state=..., interpolation=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_mask(self, img, random_state=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_bbox(self, bbox, random_state=..., **params): # -> BoxInternalType:
        ...
    
    def get_params(self): # -> dict[str, int]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['alpha'], Literal['sigma'], Literal['alpha_affine'], Literal['interpolation'], Literal['border_mode'], Literal['value'], Literal['mask_value'], Literal['approximate'], Literal['same_dxdy']]:
        ...
    


class Perspective(DualTransform):
    """Perform a random four point perspective transform of the input.

    Args:
        scale (float or (float, float)): standard deviation of the normal distributions. These are used to sample
            the random distances of the subimage's corners from the full image's corners.
            If scale is a single float value, the range will be (0, scale). Default: (0.05, 0.1).
        keep_size (bool): Whether to resize image’s back to their original size after applying the perspective
            transform. If set to False, the resulting images may end up having different shapes
            and will always be a list, never an array. Default: True
        pad_mode (OpenCV flag): OpenCV border mode.
        pad_val (int, float, list of int, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
            Default: 0
        mask_pad_val (int, float, list of int, list of float): padding value for mask
            if border_mode is cv2.BORDER_CONSTANT. Default: 0
        fit_output (bool): If True, the image plane size and position will be adjusted to still capture
            the whole image after perspective transformation. (Followed by image resizing if keep_size is set to True.)
            Otherwise, parts of the transformed image may be outside of the image plane.
            This setting should not be set to True when using large scale values as it could lead to very large images.
            Default: False
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, keypoints, bboxes

    Image types:
        uint8, float32
    """
    def __init__(self, scale=..., keep_size=..., pad_mode=..., pad_val=..., mask_pad_val=..., fit_output=..., interpolation=..., always_apply=..., p=...) -> None:
        ...
    
    def apply(self, img, matrix=..., max_height=..., max_width=..., **params): # -> ndarray[Unknown, Unknown]:
        ...
    
    def apply_to_bbox(self, bbox, matrix=..., max_height=..., max_width=..., **params): # -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint, matrix=..., max_height=..., max_width=..., **params): # -> KeypointInternalType:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_params_dependent_on_targets(self, params): # -> dict[str, Unknown | int | Any | None]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['scale'], Literal['keep_size'], Literal['pad_mode'], Literal['pad_val'], Literal['mask_pad_val'], Literal['fit_output'], Literal['interpolation']]:
        ...
    


class Affine(DualTransform):
    """Augmentation to apply affine transformations to images.
    This is mostly a wrapper around the corresponding classes and functions in OpenCV.

    Affine transformations involve:

        - Translation ("move" image on the x-/y-axis)
        - Rotation
        - Scaling ("zoom" in/out)
        - Shear (move one side of the image, turning a square into a trapezoid)

    All such transformations can create "new" pixels in the image without a defined content, e.g.
    if the image is translated to the left, pixels are created on the right.
    A method has to be defined to deal with these pixel values.
    The parameters `cval` and `mode` of this class deal with this.

    Some transformations involve interpolations between several pixels
    of the input image to generate output pixel values. The parameters `interpolation` and
    `mask_interpolation` deals with the method of interpolation used for this.

    Args:
        scale (number, tuple of number or dict): Scaling factor to use, where ``1.0`` denotes "no change" and
            ``0.5`` is zoomed out to ``50`` percent of the original size.
                * If a single number, then that value will be used for all images.
                * If a tuple ``(a, b)``, then a value will be uniformly sampled per image from the interval ``[a, b]``.
                  That the same range will be used for both x- and y-axis. To keep the aspect ratio, set
                  ``keep_ratio=True``, then the same value will be used for both x- and y-axis.
                * If a dictionary, then it is expected to have the keys ``x`` and/or ``y``.
                  Each of these keys can have the same values as described above.
                  Using a dictionary allows to set different values for the two axis and sampling will then happen
                  *independently* per axis, resulting in samples that differ between the axes. Note that when
                  the ``keep_ratio=True``, the x- and y-axis ranges should be the same.
        translate_percent (None, number, tuple of number or dict): Translation as a fraction of the image height/width
            (x-translation, y-translation), where ``0`` denotes "no change"
            and ``0.5`` denotes "half of the axis size".
                * If ``None`` then equivalent to ``0.0`` unless `translate_px` has a value other than ``None``.
                * If a single number, then that value will be used for all images.
                * If a tuple ``(a, b)``, then a value will be uniformly sampled per image from the interval ``[a, b]``.
                  That sampled fraction value will be used identically for both x- and y-axis.
                * If a dictionary, then it is expected to have the keys ``x`` and/or ``y``.
                  Each of these keys can have the same values as described above.
                  Using a dictionary allows to set different values for the two axis and sampling will then happen
                  *independently* per axis, resulting in samples that differ between the axes.
        translate_px (None, int, tuple of int or dict): Translation in pixels.
                * If ``None`` then equivalent to ``0`` unless `translate_percent` has a value other than ``None``.
                * If a single int, then that value will be used for all images.
                * If a tuple ``(a, b)``, then a value will be uniformly sampled per image from
                  the discrete interval ``[a..b]``. That number will be used identically for both x- and y-axis.
                * If a dictionary, then it is expected to have the keys ``x`` and/or ``y``.
                  Each of these keys can have the same values as described above.
                  Using a dictionary allows to set different values for the two axis and sampling will then happen
                  *independently* per axis, resulting in samples that differ between the axes.
        rotate (number or tuple of number): Rotation in degrees (**NOT** radians), i.e. expected value range is
            around ``[-360, 360]``. Rotation happens around the *center* of the image,
            not the top left corner as in some other frameworks.
                * If a number, then that value will be used for all images.
                * If a tuple ``(a, b)``, then a value will be uniformly sampled per image from the interval ``[a, b]``
                  and used as the rotation value.
        shear (number, tuple of number or dict): Shear in degrees (**NOT** radians), i.e. expected value range is
            around ``[-360, 360]``, with reasonable values being in the range of ``[-45, 45]``.
                * If a number, then that value will be used for all images as
                  the shear on the x-axis (no shear on the y-axis will be done).
                * If a tuple ``(a, b)``, then two value will be uniformly sampled per image
                  from the interval ``[a, b]`` and be used as the x- and y-shear value.
                * If a dictionary, then it is expected to have the keys ``x`` and/or ``y``.
                  Each of these keys can have the same values as described above.
                  Using a dictionary allows to set different values for the two axis and sampling will then happen
                  *independently* per axis, resulting in samples that differ between the axes.
        interpolation (int): OpenCV interpolation flag.
        mask_interpolation (int): OpenCV interpolation flag.
        cval (number or sequence of number): The constant value to use when filling in newly created pixels.
            (E.g. translating by 1px to the right will create a new 1px-wide column of pixels
            on the left of the image).
            The value is only used when `mode=constant`. The expected value range is ``[0, 255]`` for ``uint8`` images.
        cval_mask (number or tuple of number): Same as cval but only for masks.
        mode (int): OpenCV border flag.
        fit_output (bool): If True, the image plane size and position will be adjusted to tightly capture
            the whole image after affine transformation (`translate_percent` and `translate_px` are ignored).
            Otherwise (``False``),  parts of the transformed image may end up outside the image plane.
            Fitting the output shape can be useful to avoid corners of the image being outside the image plane
            after applying rotations. Default: False
        keep_ratio (bool): When True, the original aspect ratio will be kept when the random scale is applied.
                           Default: False.
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, keypoints, bboxes

    Image types:
        uint8, float32

    """
    def __init__(self, scale: Optional[Union[float, Sequence[float], dict]] = ..., translate_percent: Optional[Union[float, Sequence[float], dict]] = ..., translate_px: Optional[Union[int, Sequence[int], dict]] = ..., rotate: Optional[Union[float, Sequence[float]]] = ..., shear: Optional[Union[float, Sequence[float], dict]] = ..., interpolation: int = ..., mask_interpolation: int = ..., cval: Union[int, float, Sequence[int], Sequence[float]] = ..., cval_mask: Union[int, float, Sequence[int], Sequence[float]] = ..., mode: int = ..., fit_output: bool = ..., keep_ratio: bool = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['interpolation'], Literal['mask_interpolation'], Literal['cval'], Literal['mode'], Literal['scale'], Literal['translate_percent'], Literal['translate_px'], Literal['rotate'], Literal['fit_output'], Literal['shear'], Literal['cval_mask'], Literal['keep_ratio']]:
        ...
    
    def apply(self, img: np.ndarray, matrix: skimage.transform.ProjectiveTransform = ..., output_shape: Sequence[int] = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, matrix: skimage.transform.ProjectiveTransform = ..., output_shape: Sequence[int] = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, matrix: skimage.transform.ProjectiveTransform = ..., rows: int = ..., cols: int = ..., output_shape: Sequence[int] = ..., **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, matrix: skimage.transform.ProjectiveTransform = ..., scale: dict = ..., **params) -> KeypointInternalType:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_params_dependent_on_targets(self, params: dict) -> dict:
        ...
    


class PiecewiseAffine(DualTransform):
    """Apply affine transformations that differ between local neighbourhoods.
    This augmentation places a regular grid of points on an image and randomly moves the neighbourhood of these point
    around via affine transformations. This leads to local distortions.

    This is mostly a wrapper around scikit-image's ``PiecewiseAffine``.
    See also ``Affine`` for a similar technique.

    Note:
        This augmenter is very slow. Try to use ``ElasticTransformation`` instead, which is at least 10x faster.

    Note:
        For coordinate-based inputs (keypoints, bounding boxes, polygons, ...),
        this augmenter still has to perform an image-based augmentation,
        which will make it significantly slower and not fully correct for such inputs than other transforms.

    Args:
        scale (float, tuple of float): Each point on the regular grid is moved around via a normal distribution.
            This scale factor is equivalent to the normal distribution's sigma.
            Note that the jitter (how far each point is moved in which direction) is multiplied by the height/width of
            the image if ``absolute_scale=False`` (default), so this scale can be the same for different sized images.
            Recommended values are in the range ``0.01`` to ``0.05`` (weak to strong augmentations).
                * If a single ``float``, then that value will always be used as the scale.
                * If a tuple ``(a, b)`` of ``float`` s, then a random value will
                  be uniformly sampled per image from the interval ``[a, b]``.
        nb_rows (int, tuple of int): Number of rows of points that the regular grid should have.
            Must be at least ``2``. For large images, you might want to pick a higher value than ``4``.
            You might have to then adjust scale to lower values.
                * If a single ``int``, then that value will always be used as the number of rows.
                * If a tuple ``(a, b)``, then a value from the discrete interval
                  ``[a..b]`` will be uniformly sampled per image.
        nb_cols (int, tuple of int): Number of columns. Analogous to `nb_rows`.
        interpolation (int): The order of interpolation. The order has to be in the range 0-5:
             - 0: Nearest-neighbor
             - 1: Bi-linear (default)
             - 2: Bi-quadratic
             - 3: Bi-cubic
             - 4: Bi-quartic
             - 5: Bi-quintic
        mask_interpolation (int): same as interpolation but for mask.
        cval (number): The constant value to use when filling in newly created pixels.
        cval_mask (number): Same as cval but only for masks.
        mode (str): {'constant', 'edge', 'symmetric', 'reflect', 'wrap'}, optional
            Points outside the boundaries of the input are filled according
            to the given mode.  Modes match the behaviour of `numpy.pad`.
        absolute_scale (bool): Take `scale` as an absolute value rather than a relative value.
        keypoints_threshold (float): Used as threshold in conversion from distance maps to keypoints.
            The search for keypoints works by searching for the
            argmin (non-inverted) or argmax (inverted) in each channel. This
            parameters contains the maximum (non-inverted) or minimum (inverted) value to accept in order to view a hit
            as a keypoint. Use ``None`` to use no min/max. Default: 0.01

    Targets:
        image, mask, keypoints, bboxes

    Image types:
        uint8, float32

    """
    def __init__(self, scale: ScaleFloatType = ..., nb_rows: Union[int, Sequence[int]] = ..., nb_cols: Union[int, Sequence[int]] = ..., interpolation: int = ..., mask_interpolation: int = ..., cval: int = ..., cval_mask: int = ..., mode: str = ..., absolute_scale: bool = ..., always_apply: bool = ..., keypoints_threshold: float = ..., p: float = ...) -> None:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['scale'], Literal['nb_rows'], Literal['nb_cols'], Literal['interpolation'], Literal['mask_interpolation'], Literal['cval'], Literal['cval_mask'], Literal['mode'], Literal['absolute_scale'], Literal['keypoints_threshold']]:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_params_dependent_on_targets(self, params) -> dict:
        ...
    
    def apply(self, img: np.ndarray, matrix: skimage.transform.PiecewiseAffineTransform = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, matrix: skimage.transform.PiecewiseAffineTransform = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, rows: int = ..., cols: int = ..., matrix: skimage.transform.PiecewiseAffineTransform = ..., **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, rows: int = ..., cols: int = ..., matrix: skimage.transform.PiecewiseAffineTransform = ..., **params): # -> KeypointInternalType:
        ...
    


class PadIfNeeded(DualTransform):
    """Pad side of the image / max if side is less than desired number.

    Args:
        min_height (int): minimal result image height.
        min_width (int): minimal result image width.
        pad_height_divisor (int): if not None, ensures image height is dividable by value of this argument.
        pad_width_divisor (int): if not None, ensures image width is dividable by value of this argument.
        position (Union[str, PositionType]): Position of the image. should be PositionType.CENTER or
            PositionType.TOP_LEFT or PositionType.TOP_RIGHT or PositionType.BOTTOM_LEFT or PositionType.BOTTOM_RIGHT.
            or PositionType.RANDOM. Default: PositionType.CENTER.
        border_mode (OpenCV flag): OpenCV border mode.
        value (int, float, list of int, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
        mask_value (int, float,
                    list of int,
                    list of float): padding value for mask if border_mode is cv2.BORDER_CONSTANT.
        p (float): probability of applying the transform. Default: 1.0.

    Targets:
        image, mask, bbox, keypoints

    Image types:
        uint8, float32
    """
    class PositionType(Enum):
        CENTER = ...
        TOP_LEFT = ...
        TOP_RIGHT = ...
        BOTTOM_LEFT = ...
        BOTTOM_RIGHT = ...
        RANDOM = ...
    
    
    def __init__(self, min_height: Optional[int] = ..., min_width: Optional[int] = ..., pad_height_divisor: Optional[int] = ..., pad_width_divisor: Optional[int] = ..., position: Union[PositionType, str] = ..., border_mode: int = ..., value: Optional[ImageColorType] = ..., mask_value: Optional[ImageColorType] = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def update_params(self, params, **kwargs): # -> Dict[str, Any]:
        ...
    
    def apply(self, img: np.ndarray, pad_top: int = ..., pad_bottom: int = ..., pad_left: int = ..., pad_right: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, pad_top: int = ..., pad_bottom: int = ..., pad_left: int = ..., pad_right: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, pad_top: int = ..., pad_bottom: int = ..., pad_left: int = ..., pad_right: int = ..., rows: int = ..., cols: int = ..., **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, pad_top: int = ..., pad_bottom: int = ..., pad_left: int = ..., pad_right: int = ..., **params) -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['min_height'], Literal['min_width'], Literal['pad_height_divisor'], Literal['pad_width_divisor'], Literal['border_mode'], Literal['value'], Literal['mask_value']]:
        ...
    


class VerticalFlip(DualTransform):
    """Flip the input vertically around the x-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, **params) -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[()]:
        ...
    


class HorizontalFlip(DualTransform):
    """Flip the input horizontally around the y-axis.

    Args:
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, **params) -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[()]:
        ...
    


class Flip(DualTransform):
    """Flip the input either horizontally, vertically or both horizontally and vertically.

    Args:
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def apply(self, img: np.ndarray, d: int = ..., **params) -> np.ndarray:
        """Args:
        d (int): code that specifies how to flip the input. 0 for vertical flipping, 1 for horizontal flipping,
                -1 for both vertical and horizontal flipping (which is also could be seen as rotating the input by
                180 degrees).
        """
        ...
    
    def get_params(self): # -> dict[str, int]:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, **params) -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[()]:
        ...
    


class Transpose(DualTransform):
    """Transpose the input by swapping rows and columns.

    Args:
        p (float): probability of applying the transform. Default: 0.5.

    Targets:
        image, mask, bboxes, keypoints

    Image types:
        uint8, float32
    """
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, **params) -> BoxInternalType:
        ...
    
    def apply_to_keypoint(self, keypoint: KeypointInternalType, **params) -> KeypointInternalType:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[()]:
        ...
    


class OpticalDistortion(DualTransform):
    """
    Args:
        distort_limit (float, (float, float)): If distort_limit is a single float, the range
            will be (-distort_limit, distort_limit). Default: (-0.05, 0.05).
        shift_limit (float, (float, float))): If shift_limit is a single float, the range
            will be (-shift_limit, shift_limit). Default: (-0.05, 0.05).
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        border_mode (OpenCV flag): flag that is used to specify the pixel extrapolation method. Should be one of:
            cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, cv2.BORDER_REFLECT_101.
            Default: cv2.BORDER_REFLECT_101
        value (int, float, list of ints, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
        mask_value (int, float,
                    list of ints,
                    list of float): padding value if border_mode is cv2.BORDER_CONSTANT applied for masks.

    Targets:
        image, mask, bbox

    Image types:
        uint8, float32
    """
    def __init__(self, distort_limit: ScaleFloatType = ..., shift_limit: ScaleFloatType = ..., interpolation: int = ..., border_mode: int = ..., value: Optional[ImageColorType] = ..., mask_value: Optional[ImageColorType] = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, k: int = ..., dx: int = ..., dy: int = ..., interpolation: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, k: int = ..., dx: int = ..., dy: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, k: int = ..., dx: int = ..., dy: int = ..., **params) -> BoxInternalType:
        ...
    
    def get_params(self): # -> dict[str, float | int]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['distort_limit'], Literal['shift_limit'], Literal['interpolation'], Literal['border_mode'], Literal['value'], Literal['mask_value']]:
        ...
    


class GridDistortion(DualTransform):
    """
    Args:
        num_steps (int): count of grid cells on each side.
        distort_limit (float, (float, float)): If distort_limit is a single float, the range
            will be (-distort_limit, distort_limit). Default: (-0.03, 0.03).
        interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
            cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
            Default: cv2.INTER_LINEAR.
        border_mode (OpenCV flag): flag that is used to specify the pixel extrapolation method. Should be one of:
            cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, cv2.BORDER_REFLECT_101.
            Default: cv2.BORDER_REFLECT_101
        value (int, float, list of ints, list of float): padding value if border_mode is cv2.BORDER_CONSTANT.
        mask_value (int, float,
                    list of ints,
                    list of float): padding value if border_mode is cv2.BORDER_CONSTANT applied for masks.
        normalized (bool): if true, distortion will be normalized to do not go outside the image. Default: False
            See for more information: https://github.com/albumentations-team/albumentations/pull/722

    Targets:
        image, mask

    Image types:
        uint8, float32
    """
    def __init__(self, num_steps: int = ..., distort_limit: ScaleFloatType = ..., interpolation: int = ..., border_mode: int = ..., value: Optional[ImageColorType] = ..., mask_value: Optional[ImageColorType] = ..., normalized: bool = ..., always_apply: bool = ..., p: float = ...) -> None:
        ...
    
    def apply(self, img: np.ndarray, stepsx: Tuple = ..., stepsy: Tuple = ..., interpolation: int = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_mask(self, img: np.ndarray, stepsx: Tuple = ..., stepsy: Tuple = ..., **params) -> np.ndarray:
        ...
    
    def apply_to_bbox(self, bbox: BoxInternalType, stepsx: Tuple = ..., stepsy: Tuple = ..., **params) -> BoxInternalType:
        ...
    
    @property
    def targets_as_params(self): # -> list[str]:
        ...
    
    def get_params_dependent_on_targets(self, params): # -> dict[str, Unknown] | dict[str, list[float]]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['num_steps'], Literal['distort_limit'], Literal['interpolation'], Literal['border_mode'], Literal['value'], Literal['mask_value'], Literal['normalized']]:
        ...
    


