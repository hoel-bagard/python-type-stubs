from typing import Any, Callable

import numpy as np
from matplotlib import _api
from matplotlib._typing import *
from matplotlib.backend_bases import (FigureCanvasBase, FigureManagerBase,
                                      GraphicsContextBase, RendererBase,
                                      _Backend)
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
from matplotlib.transforms import Affine2DBase, Transform

class __getattr__:
    NO_ESCAPE = ...
    re_mathsep = ...

def get_fontspec() -> str: ...
def get_preamble() -> str: ...

latex_pt_to_in: float = ...
latex_in_to_pt: float = ...
mpl_pt_to_in: float = ...
mpl_in_to_pt: float = ...

def common_texification(text)-> str: ...
def writeln(fh, line)-> None: ...
def make_pdf_to_png_converter() -> Callable: ...

class LatexError(Exception):
    def __init__(self, message, latex_output=...) -> None: ...
    def __str__(self) -> str: ...

class LatexManager:
    def __init__(self) -> None: ...

    str_cache = ...
    def get_width_height_descent(self, text, prop) -> tuple[float, float, float]: ...

class RendererPgf(RendererBase):
    def __init__(self, figure: Figure, fh: FileLike) -> None: ...
    def draw_markers(
        self,
        gc: GraphicsContextBase,
        marker_path,
        marker_trans: Transform,
        path,
        trans: Transform,
        rgbFace=...,
    )-> None: ...
    def draw_path(self, gc, path, transform, rgbFace=...)-> None: ...
    def option_scale_image(self)-> bool: ...
    def option_image_nocomposite(self)-> bool: ...
    def draw_image(
        self,
        gc: GraphicsContextBase,
        x: Scalar,
        y: Scalar,
        im,
        transform: Affine2DBase = ...,
    )-> None: ...
    def draw_tex(self, gc, x, y, s, prop, angle, ismath=..., mtext=...)-> None: ...
    def draw_text(
        self,
        gc: GraphicsContextBase,
        x: float,
        y: float,
        s: str,
        prop: FontProperties,
        angle: float,
        ismath=...,
        mtext: Text = ...,
    )-> None: ...
    def get_text_width_height_descent(
        self, s: str, prop: FontProperties, ismath: str
    )-> tuple[float, float, float]: ...
    def flipy(self)-> bool: ...
    def get_canvas_width_height(self)-> tuple[float, float]: ...
    def points_to_pixels(self, points: float | ArrayLike): ...

class FigureCanvasPgf(FigureCanvasBase):
    filetypes: dict[str, str] = ...
    def get_default_filetype(self)-> str: ...
    def print_pgf(self, fname_or_fh, **kwargs) -> None: ...
    def print_pdf(self, fname_or_fh, *, metadata=..., **kwargs) -> None: ...
    def print_png(self, fname_or_fh, **kwargs) -> None: ...
    def get_renderer(self) -> RendererPgf: ...
    def draw(self)-> None: ...

FigureManagerPgf = FigureManagerBase

class _BackendPgf(_Backend):
    FigureCanvas = FigureCanvasPgf

class PdfPages:
    def __init__(
        self,
        filename: str | PathLike,
        *,
        keep_empty: bool = True,
        metadata: dict[str, Any] = ...
    ) -> None: ...
    def __enter__(self)-> PdfPages: ...
    def __exit__(self, exc_type, exc_val, exc_tb)-> None: ...
    def close(self) -> None: ...
    def savefig(self, figure: Figure | int = ..., **kwargs) -> None: ...
    def get_pagecount(self) -> int: ...
