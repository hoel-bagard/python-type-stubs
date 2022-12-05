from typing import Literal, Sequence

import numpy as np
from PIL.Image import Image

from ._typing import *
from .artist import Artist, allow_rasterization
from .axes import Axes
from .backend_bases import MouseEvent, RendererBase
from .cm import ScalarMappable
from .colors import Colormap, Normalize
from .figure import Figure
from .transforms import Affine2D, Bbox

interpolations_names = ...

def composite_images(
    images: list[Image], renderer: RendererBase, magnification: float = 1
) -> tuple[np.ndarray, tuple[float, float]]: ...

class _ImageBase(Artist, ScalarMappable):

    zorder = ...
    def __init__(
        self,
        ax: Axes,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        *,
        interpolation_stage=...,
        **kwargs
    ) -> None: ...
    def __str__(self) -> str: ...
    def __getstate__(self): ...
    def get_size(self): ...
    def set_alpha(self, alpha: float | ArrayLike | None)-> None: ...
    def changed(self)-> bool: ...
    def make_image(
        self, renderer, magnification=..., unsampled=...
    ) -> tuple[np.ndarray, tuple[float, float], Affine2D]: ...
    @allow_rasterization
    def draw(self, renderer: RendererBase, *args, **kwargs)-> None: ...
    def contains(self, mouseevent: MouseEvent)-> bool: ...
    def write_png(self, fname: str)-> None: ...
    def set_data(self, A: ArrayLike | Image)-> None: ...
    def set_array(self, A: ArrayLike)-> None: ...
    def get_interpolation(self) -> str: ...
    def set_interpolation(
        self,
        s: Literal[
            "antialiased",
            "nearest",
            "bilinear",
            "bicubic",
            "spline16",
            "spline36",
            "hanning",
            "hamming",
            "hermite",
            "kaiser",
            "quadric",
            "catrom",
            "gaussian",
            "bessel",
            "mitchell",
            "sinc",
            "lanczos",
            "none",
        ]
        | None,
    )-> None: ...
    def set_interpolation_stage(self, s: Literal["data", "rgba"] | None)-> None: ...
    def can_composite(self) -> bool: ...
    def set_resample(self, v: bool | None)-> None: ...
    def get_resample(self) -> bool: ...
    def set_filternorm(self, filternorm: bool)-> None: ...
    def get_filternorm(self) -> bool: ...
    def set_filterrad(self, filterrad: float)-> None: ...
    def get_filterrad(self) -> float: ...

class AxesImage(_ImageBase):
    def __init__(
        self,
        ax: Axes,
        cmap: str | Colormap = ...,
        norm: Normalize = ...,
        interpolation: str = ...,
        origin: Literal["upper", "lower"] = ...,
        extent: tuple = ...,
        filternorm: bool = True,
        filterrad: float = 4,
        resample: bool = False,
        *,
        interpolation_stage: Literal["data", "rgba"] = ...,
        **kwargs
    ) -> None: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_extent(self, extent: Sequence[float])-> None: ...
    def get_extent(self) -> tuple[float, float, float, float]: ...
    def get_cursor_data(self, event: MouseEvent): ...

class NonUniformImage(AxesImage):
    mouseover = ...
    def __init__(
        self,
        ax: Axes,
        *,
        interpolation: Literal["nearest", "bilinear"] = "nearest",
        **kwargs
    ) -> None: ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike)-> None: ...
    def set_array(self, *args)-> None: ...
    def set_interpolation(self, s: Literal["nearest", "bilinear"] | None)-> None: ...
    def get_extent(self): ...
    def set_filternorm(self, s)-> None: ...
    def set_filterrad(self, s)-> None: ...
    def set_norm(self, norm: Normalize | None)-> None: ...
    def set_cmap(self, cmap: Colormap | str | None)-> None: ...

class PcolorImage(AxesImage):
    def __init__(
        self,
        ax: Axes,
        x: ArrayLike = ...,
        y: ArrayLike = ...,
        A: ArrayLike = ...,
        cmap: str | Colormap = ...,
        norm: Normalize = ...,
        **kwargs
    ) -> None: ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike)-> None: ...
    def set_array(self, *args)-> None: ...
    def get_cursor_data(self, event: MouseEvent): ...

class FigureImage(_ImageBase):

    zorder = ...

    def __init__(
        self,
        fig: Figure,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        offsetx=...,
        offsety=...,
        origin=...,
        **kwargs
    ) -> None: ...
    def get_extent(self) -> tuple[float, float, float, float]: ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, A)-> None: ...

class BboxImage(_ImageBase):
    def __init__(
        self,
        bbox: Bbox,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        **kwargs
    ) -> None: ...
    def get_window_extent(
        self, renderer: RendererBase = ...
    ) -> tuple[float, float, float, float]: ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...

def imread(fname: str | FileLike, format: str = ...) -> np.ndarray: ...
def imsave(
    fname: str | PathLike | FileLike,
    arr: ArrayLike,
    vmin: float = ...,
    vmax: float = ...,
    cmap: str | Colormap = ...,
    format: str = ...,
    origin: Literal["upper", "lower"] = ...,
    dpi: float = ...,
    *,
    metadata: dict = ...,
    pil_kwargs: dict = ...
): ...
def pil_to_array(pilImage) -> np.ndarray: ...
def thumbnail(
    infile: str | FileLike,
    thumbfile: str | FileLike,
    scale: float = ...,
    interpolation: str = ...,
    preview: bool = ...,
) -> Figure: ...
