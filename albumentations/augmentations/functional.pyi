"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Optional, Sequence, Union
from albumentations.augmentations.utils import clipped, ensure_contiguous, preserve_channel_dim, preserve_shape

__all__ = ["add_fog", "add_rain", "add_shadow", "add_snow", "add_sun_flare", "add_weighted", "adjust_brightness_torchvision", "adjust_contrast_torchvision", "adjust_hue_torchvision", "adjust_saturation_torchvision", "brightness_contrast_adjust", "channel_shuffle", "clahe", "convolve", "downscale", "equalize", "fancy_pca", "from_float", "gamma_transform", "gauss_noise", "image_compression", "invert", "iso_noise", "linear_transformation_rgb", "move_tone_curve", "multiply", "noop", "normalize", "posterize", "shift_hsv", "shift_rgb", "solarize", "superpixels", "swap_tiles_on_image", "to_float", "to_gray", "unsharp_mask"]
def normalize_cv2(img, mean, denominator): # -> NDArray[Unknown]:
    ...

def normalize_numpy(img, mean, denominator):
    ...

def normalize(img, mean, std, max_pixel_value=...): # -> NDArray[Unknown]:
    ...

@preserve_shape
def shift_hsv(img, hue_shift, sat_shift, val_shift): # -> NDArray[Unknown]:
    ...

def solarize(img, threshold=...): # -> NDArray[Unknown]:
    """Invert all pixel values above a threshold.

    Args:
        img (numpy.ndarray): The image to solarize.
        threshold (int): All pixels above this greyscale level are inverted.

    Returns:
        numpy.ndarray: Solarized image.

    """
    ...

@preserve_shape
def posterize(img, bits):
    """Reduce the number of bits for each color channel.

    Args:
        img (numpy.ndarray): image to posterize.
        bits (int): number of high bits. Must be in range [0, 8]

    Returns:
        numpy.ndarray: Image with reduced color channels.

    """
    ...

@preserve_channel_dim
def equalize(img, mask=..., mode=..., by_channels=...): # -> NDArray[Unknown]:
    """Equalize the image histogram.

    Args:
        img (numpy.ndarray): RGB or grayscale image.
        mask (numpy.ndarray): An optional mask.  If given, only the pixels selected by
            the mask are included in the analysis. Maybe 1 channel or 3 channel array.
        mode (str): {'cv', 'pil'}. Use OpenCV or Pillow equalization method.
        by_channels (bool): If True, use equalization by channels separately,
            else convert image to YCbCr representation and use equalization by `Y` channel.

    Returns:
        numpy.ndarray: Equalized image.

    """
    ...

@preserve_shape
def move_tone_curve(img, low_y, high_y): # -> ndarray[Unknown, Unknown]:
    """Rescales the relationship between bright and dark areas of the image by manipulating its tone curve.

    Args:
        img (numpy.ndarray): RGB or grayscale image.
        low_y (float): y-position of a Bezier control point used
            to adjust the tone curve, must be in range [0, 1]
        high_y (float): y-position of a Bezier control point used
            to adjust image tone curve, must be in range [0, 1]
    """
    ...

def shift_rgb(img, r_shift, g_shift, b_shift): # -> ndarray[Unknown, Unknown]:
    ...

@clipped
def linear_transformation_rgb(img, transformation_matrix):
    ...

@preserve_channel_dim
def clahe(img, clip_limit=..., tile_grid_size=...): # -> NDArray[Unknown]:
    ...

@preserve_shape
def convolve(img, kernel): # -> ndarray[Unknown, Unknown]:
    ...

@preserve_shape
def image_compression(img, quality, image_type):
    ...

@preserve_shape
def add_snow(img, snow_point, brightness_coeff): # -> NDArray[floating[Any]] | NDArray[uint8]:
    """Bleaches out pixels, imitation snow.

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img (numpy.ndarray): Image.
        snow_point: Number of show points.
        brightness_coeff: Brightness coefficient.

    Returns:
        numpy.ndarray: Image.

    """
    ...

@preserve_shape
def add_rain(img, slant, drop_length, drop_width, drop_color, blur_value, brightness_coefficient, rain_drops): # -> NDArray[floating[Any]] | NDArray[uint8]:
    """

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img (numpy.ndarray): Image.
        slant (int):
        drop_length:
        drop_width:
        drop_color:
        blur_value (int): Rainy view are blurry.
        brightness_coefficient (float): Rainy days are usually shady.
        rain_drops:

    Returns:
        numpy.ndarray: Image.

    """
    ...

@preserve_shape
def add_fog(img, fog_coef, alpha_coef, haze_list):
    """Add fog to the image.

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img (numpy.ndarray): Image.
        fog_coef (float): Fog coefficient.
        alpha_coef (float): Alpha coefficient.
        haze_list (list):

    Returns:
        numpy.ndarray: Image.

    """
    ...

@preserve_shape
def add_sun_flare(img, flare_center_x, flare_center_y, src_radius, src_color, circles):
    """Add sun flare.

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img (numpy.ndarray):
        flare_center_x (float):
        flare_center_y (float):
        src_radius:
        src_color (int, int, int):
        circles (list):

    Returns:
        numpy.ndarray:

    """
    ...

@ensure_contiguous
@preserve_shape
def add_shadow(img, vertices_list): # -> NDArray[floating[Any]] | NDArray[Unknown]:
    """Add shadows to the image.

    From https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library

    Args:
        img (numpy.ndarray):
        vertices_list (list):

    Returns:
        numpy.ndarray:

    """
    ...

def invert(img: np.ndarray) -> np.ndarray:
    ...

def channel_shuffle(img, channels_shuffled):
    ...

@preserve_shape
def gamma_transform(img, gamma): # -> Any:
    ...

@clipped
def gauss_noise(image, gauss):
    ...

def brightness_contrast_adjust(img, alpha=..., beta=..., beta_by_max=...): # -> ndarray[Unknown, Unknown]:
    ...

@clipped
def iso_noise(image, color_shift=..., intensity=..., random_state=..., **kwargs): # -> NDArray[uint8]:
    """
    Apply poisson noise to image to simulate camera sensor noise.

    Args:
        image (numpy.ndarray): Input image, currently, only RGB, uint8 images are supported.
        color_shift (float):
        intensity (float): Multiplication factor for noise values. Values of ~0.5 are produce noticeable,
                   yet acceptable level of noise.
        random_state:
        **kwargs:

    Returns:
        numpy.ndarray: Noised image

    """
    ...

def to_gray(img): # -> NDArray[Unknown]:
    ...

@preserve_shape
def downscale(img, scale, down_interpolation=..., up_interpolation=...): # -> NDArray[uint8] | NDArray[Unknown]:
    ...

def to_float(img, max_value=...):
    ...

def from_float(img, dtype, max_value=...):
    ...

def noop(input_obj, **params):
    ...

def swap_tiles_on_image(image, tiles):
    """
    Swap tiles on image.

    Args:
        image (np.ndarray): Input image.
        tiles (np.ndarray): array of tuples(
            current_left_up_corner_row, current_left_up_corner_col,
            old_left_up_corner_row, old_left_up_corner_col,
            height_tile, width_tile)

    Returns:
        np.ndarray: Output image.

    """
    ...

def multiply(img, multiplier): # -> ndarray[Unknown, Unknown]:
    """
    Args:
        img (numpy.ndarray): Image.
        multiplier (numpy.ndarray): Multiplier coefficient.

    Returns:
        numpy.ndarray: Image multiplied by `multiplier` coefficient.

    """
    ...

def bbox_from_mask(mask): # -> tuple[Literal[-1], Literal[-1], Literal[-1], Literal[-1]] | tuple[Any, Any, Any, Any]:
    """Create bounding box from binary mask (fast version)

    Args:
        mask (numpy.ndarray): binary mask.

    Returns:
        tuple: A bounding box tuple `(x_min, y_min, x_max, y_max)`.

    """
    ...

def mask_from_bbox(img, bbox): # -> NDArray[uint8]:
    """Create binary mask from bounding box

    Args:
        img (numpy.ndarray): input image
        bbox: A bounding box tuple `(x_min, y_min, x_max, y_max)`

    Returns:
        mask (numpy.ndarray): binary mask

    """
    ...

def fancy_pca(img, alpha=...):
    """Perform 'Fancy PCA' augmentation from:
    http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf

    Args:
        img (numpy.ndarray): numpy array with (h, w, rgb) shape, as ints between 0-255
        alpha (float): how much to perturb/scale the eigen vecs and vals
                the paper used std=0.1

    Returns:
        numpy.ndarray: numpy image-like array as uint8 range(0, 255)

    """
    ...

@preserve_shape
def adjust_brightness_torchvision(img, factor): # -> ndarray[Unknown, Unknown]:
    ...

@preserve_shape
def adjust_contrast_torchvision(img, factor): # -> ndarray[Unknown, Unknown]:
    ...

@preserve_shape
def adjust_saturation_torchvision(img, factor, gamma=...): # -> NDArray[Unknown] | ndarray[Unknown, Unknown]:
    ...

def adjust_hue_torchvision(img, factor): # -> NDArray[Unknown]:
    ...

@preserve_shape
def superpixels(image: np.ndarray, n_segments: int, replace_samples: Sequence[bool], max_size: Optional[int], interpolation: int) -> np.ndarray:
    ...

@clipped
def add_weighted(img1, alpha, img2, beta):
    ...

@clipped
@preserve_shape
def unsharp_mask(image: np.ndarray, ksize: int, sigma: float = ..., alpha: float = ..., threshold: int = ...): # -> NDArray[uint8]:
    ...

@preserve_shape
def pixel_dropout(image: np.ndarray, drop_mask: np.ndarray, drop_value: Union[float, Sequence[float]]) -> np.ndarray:
    ...

@clipped
@preserve_shape
def spatter(img: np.ndarray, non_mud: Optional[np.ndarray], mud: Optional[np.ndarray], rain: Optional[np.ndarray], mode: str) -> np.ndarray:
    ...

