import functools
from collections.abc import Mapping
from email.errors import NonPrintableDefect
from re import Pattern
from typing import Callable, Iterator, Literal

import numpy as np
from matplotlib._typing import *

from .scale import AsinhScale, FuncScale, LogScale, SymmetricalLogScale

class _ColorMapping(dict):
    def __init__(self, mapping) -> None: ...
    def __setitem__(self, key, value)-> None: ...
    def __delitem__(self, key)-> None: ...

def get_named_colors_mapping()-> _ColorMapping: ...

class ColorSequenceRegistry(Mapping):
    def __init__(self) -> None: ...
    def __getitem__(self, item)-> list[Color]: ...
    def __iter__(self)-> Iterator[Color]: ...
    def __len__(self)-> int: ...
    def __str__(self) -> str: ...
    def register(self, name: str, color_list: list[Color])-> None: ...
    def unregister(self, name)-> None: ...

def is_color_like(c)-> bool: ...
def same_color(c1: Color, c2: Color)-> bool: ...
def to_rgba(c: np.ma.masked_array, alpha: float = ...) -> tuple: ...
def to_rgba_array(c: ArrayLike, alpha: float = ...) -> list: ...
def to_rgb(c: Color)-> tuple: ...
def to_hex(c: Color, keep_alpha: bool = ...) -> str: ...

cnames: dict[str, str] = ...
hexColorPattern: Pattern[str] = ...
rgb2hex = to_hex
hex2color = to_rgb

class ColorConverter:

    colors: _ColorMapping = ...
    cache: dict = ...
    @staticmethod
    def to_rgb(c: Color)-> tuple: ...
    @staticmethod
    def to_rgba(c: np.ma.masked_array, alpha: float = ...) -> tuple: ...
    @staticmethod
    def to_rgba_array(c: ArrayLike, alpha: float = ...) -> list: ...

colorConverter: ColorConverter = ...

class Colormap:
    def __init__(self, name: str, N:int=256) -> None: ...
    def __call__(
        self,
        X: float | int | np.ndarray | Scalar,
        alpha: float | ArrayLike | None = None,
        bytes: bool = False,
    ) -> tuple: ...
    def __copy__(self)-> Colormap: ...
    def __eq__(self, other: Colormap) -> bool: ...
    def get_bad(self)-> np.ndarray: ...
    def set_bad(self, color: Color='k', alpha: float|None=None): ...
    def get_under(self)-> np.ndarray: ...
    def set_under(self, color: Color='k', alpha: float|None=None): ...
    def get_over(self)-> np.ndarray: ...
    def set_over(self, color: Color='k', alpha: float|None=None): ...
    def set_extremes(self, *, bad=None, under=None, over=None)-> None: ...
    def with_extremes(self, *, bad=None, under: None=..., over: None=...)-> None: ...
    def is_gray(self)-> bool: ...
    def reversed(self, name: str|None = None)-> Colormap: ...
    def copy(self): ...

class LinearSegmentedColormap(Colormap):
    def __init__(self, name, segmentdata, N=..., gamma=...) -> None: ...
    def set_gamma(self, gamma)-> NonPrintableDefect: ...
    @staticmethod
    def from_list(name: str, colors, N: int = ..., gamma: float = ...)-> LinearSegmentedColormap: ...
    def reversed(self, name: str = ...) -> LinearSegmentedColormap: ...

class ListedColormap(Colormap):
    def __init__(self, colors: list, array, name: str = ..., N: int = ...) -> None: ...
    def reversed(self, name: str = ...) -> ListedColormap: ...

class Normalize:
    def __init__(self, vmin=..., vmax=..., clip=...) -> None: ...
    @property
    def vmin(self)-> float: ...
    @vmin.setter
    def vmin(self, value: float)-> None: ...
    @property
    def vmax(self)-> float: ...
    @vmax.setter
    def vmax(self, value: float)-> None: ...
    @property
    def clip(self)-> bool: ...
    @clip.setter
    def clip(self, value: bool)-> None: ...
    @staticmethod
    def process_value(value)-> tuple[np.ndarray, bool]: ...
    def __call__(self, value, clip: bool|None = None): ...
    def inverse(self, value): ...
    def autoscale(self, A)-> None: ...
    def autoscale_None(self, A)-> None: ...
    def scaled(self)-> bool: ...

class TwoSlopeNorm(Normalize):
    def __init__(self, vcenter, vmin=..., vmax=...) -> None: ...
    @property
    def vcenter(self): ...
    @vcenter.setter
    def vcenter(self, value)-> None: ...
    def autoscale_None(self, A)-> None: ...
    def __call__(self, value, clip=...): ...
    def inverse(self, value): ...

class CenteredNorm(Normalize):
    def __init__(self, vcenter=..., halfrange=..., clip=...) -> None: ...
    def autoscale(self, A)-> None: ...
    def autoscale_None(self, A)-> None: ...
    @property
    def vcenter(self): ...
    @vcenter.setter
    def vcenter(self, vcenter)-> None: ...
    @property
    def halfrange(self): ...
    @halfrange.setter
    def halfrange(self, halfrange)-> None: ...
    def __call__(self, value, clip: bool = ...): ...

def make_norm_from_scale(scale_cls, base_norm_cls=..., *, init=...): ...
@make_norm_from_scale(
    FuncScale, init=lambda functions, vmin=None, vmax=None, clip=False: None
)
class FuncNorm(Normalize): ...

@make_norm_from_scale(functools.partial(LogScale, nonpositive="mask"))
class LogNorm(Normalize): ...

@make_norm_from_scale(
    SymmetricalLogScale,
    init=lambda linthresh, linscale=1, vmin=None, vmax=None, clip=False, *, base=10: None,
)
class SymLogNorm(Normalize):
    @property
    def linthresh(self): ...
    @linthresh.setter
    def linthresh(self, value): ...

@make_norm_from_scale(
    AsinhScale, init=lambda linear_width=1, vmin=None, vmax=None, clip=False: None
)
class AsinhNorm(Normalize):
    @property
    def linear_width(self): ...
    @linear_width.setter
    def linear_width(self, value)-> None: ...

class PowerNorm(Normalize):
    def __init__(self, gamma, vmin=..., vmax=..., clip=...) -> None: ...
    def __call__(self, value, clip: bool = ...): ...
    def inverse(self, value): ...

class BoundaryNorm(Normalize):
    def __init__(self, boundaries, ncolors, clip=..., *, extend=...) -> None: ...
    def __call__(self, value, clip=...): ...
    def inverse(self, value): ...

class NoNorm(Normalize):
    def __call__(self, value, clip: bool = ...): ...
    def inverse(self, value): ...

def rgb_to_hsv(arr): ...
def hsv_to_rgb(hsv): ...

class LightSource:
    def __init__(
        self,
        azdeg=...,
        altdeg=...,
        hsv_min_val=...,
        hsv_max_val=...,
        hsv_min_sat=...,
        hsv_max_sat=...,
    ) -> None: ...
    @property
    def direction(self): ...
    def hillshade(
        self,
        elevation,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
    ) -> np.ndarray: ...
    def shade_normals(self, normals, fraction: float = ...) -> np.ndarray: ...
    def shade(
        self,
        data,
        cmap: Colormap,
        norm=...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vmin: float | None = ...,
        vmax: float | None = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
        **kwargs
    ) -> np.ndarray: ...
    def shade_rgb(
        self,
        rgb: ArrayLike,
        elevation: ArrayLike,
        fraction: float = ...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        **kwargs
    ) -> np.ndarray: ...
    def blend_hsv(
        self,
        rgb: np.ndarray,
        intensity: np.ndarray,
        hsv_max_sat: float = ...,
        hsv_max_val: float = ...,
        hsv_min_val: float = ...,
        hsv_min_sat: float = ...,
    ) -> np.ndarray: ...
    def blend_soft_light(
        self, rgb: np.ndarray, intensity: np.ndarray
    ) -> np.ndarray: ...
    def blend_overlay(self, rgb: np.ndarray, intensity: np.ndarray) -> np.ndarray: ...

def from_levels_and_colors(
    levels, colors, extend: Literal["neither", "min", "max", "both"] = ...
): ...
