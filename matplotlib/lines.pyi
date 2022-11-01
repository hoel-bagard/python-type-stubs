from typing import Any, Callable, Literal, Sequence

import numpy as np
from matplotlib.markers import MarkerStyle

from ._enums import CapStyle, JoinStyle
from ._typing import *
from .artist import allow_rasterization, Artist
from .backend_bases import Event, MouseEvent, RendererBase
from .backends.backend_agg import RendererAgg
from .path import Path
from .transforms import Bbox, Transform

def segment_hits(cx, cy, x, y, radius): ...

class Line2D(Artist):

    lineStyles = ...

    drawStyles = ...
    drawStyleKeys = ...
    markers = ...
    filled_markers = ...
    fillStyles = ...
    zorder = ...
    def __str__(self) -> str: ...
    def __init__(
        self,
        xdata: Sequence[float],
        ydata: Sequence[float],
        linewidth: float = ...,
        linestyle=...,
        color: Color = ...,
        marker: str = ...,
        markersize: float = ...,
        markeredgewidth: float = ...,
        markeredgecolor: Color = ...,
        markerfacecolor: Color = ...,
        markerfacecoloralt: Color = ...,
        fillstyle: Literal["full", "left", "right", "bottom", "top", "none"] = ...,
        antialiased: bool = ...,
        dash_capstyle: CapStyle = ...,
        solid_capstyle: CapStyle = ...,
        dash_joinstyle: JoinStyle = ...,
        solid_joinstyle: JoinStyle = ...,
        pickradius: float = ...,
        drawstyle: Literal[
            "default", "steps", "steps-pre", "steps-mid", "steps-post"
        ] = "default",
        markevery=...,
        **kwargs
    ) -> None: ...
    def contains(self, mouseevent: MouseEvent): ...
    def get_pickradius(self) -> float: ...
    def set_pickradius(self, d: float) -> None: ...
    pickradius = ...
    def get_fillstyle(self) -> str: ...
    def set_fillstyle(
        self, fs: Literal["full", "left", "right", "bottom", "top", "none"]
    )-> None: ...
    def set_markevery(self, every) -> None: ...
    def get_markevery(self) -> Any: ...
    def set_picker(self, p: Callable | float) -> None: ...
    def get_bbox(self) -> Bbox: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def set_data(self, *args) -> None: ...
    def recache_always(self) -> bool: ...
    def recache(self, always: bool = ...) -> None: ...
    def set_transform(self, t: Transform): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def get_antialiased(self) -> bool: ...
    def get_color(self) -> str: ...
    def get_drawstyle(self) -> str: ...
    def get_linestyle(self) -> str: ...
    def get_linewidth(self) -> float: ...
    def get_marker(self) -> int | str: ...
    def get_markeredgecolor(self) -> Color: ...
    def get_markeredgewidth(self) -> float: ...
    def get_markerfacecolor(self) -> Color: ...
    def get_markerfacecoloralt(self) -> Color: ...
    def get_markersize(self) -> float: ...
    def get_data(
        self, orig: bool = False
    ) -> tuple[Sequence[float], Sequence[float]]: ...
    def get_xdata(self, orig: bool = False) -> Sequence[float]: ...
    def get_ydata(self, orig: bool = False) -> Sequence[float]: ...
    def get_path(self) -> Path: ...
    def get_xydata(self) -> np.ndarray: ...
    def set_antialiased(self, b: bool) -> None: ...
    def set_color(self, color: Color) -> None: ...
    def set_drawstyle(
        self,
        drawstyle: Literal[
            "default", "steps", "steps-pre", "steps-mid", "steps-post"
        ] = "default",
    ) -> None: ...
    def set_linewidth(self, w: float) -> None: ...
    def set_linestyle(self, ls: Any) -> None: ...
    def set_marker(self, marker: str | Path | MarkerStyle) -> None: ...
    def set_markeredgecolor(self, ec: Color) -> None: ...
    def set_markerfacecolor(self, fc: Color) -> None: ...
    def set_markerfacecoloralt(self, fc: Color) -> None: ...
    def set_markeredgewidth(self, ew: float) -> None: ...
    def set_markersize(self, sz: float) -> None: ...
    def set_xdata(self, x: ArrayLike) -> None: ...
    def set_ydata(self, y: ArrayLike) -> None: ...
    def set_dashes(self, seq: Sequence[int]) -> None: ...
    def update_from(self, other: Line2D) -> None: ...
    def set_dash_joinstyle(self, s: JoinStyle) -> None: ...
    def set_solid_joinstyle(self, s: JoinStyle | str) -> None: ...
    def get_dash_joinstyle(self) -> JoinStyle | str: ...
    def get_solid_joinstyle(self) -> JoinStyle | str: ...
    def set_dash_capstyle(self, s: CapStyle | str) -> None: ...
    def set_solid_capstyle(self, s: CapStyle | str) -> None: ...
    def get_dash_capstyle(self) -> CapStyle | str: ...
    def get_solid_capstyle(self) -> CapStyle | str: ...
    def is_dashed(self) -> bool: ...

class _AxLine(Line2D):
    def __init__(
        self, xy1: Sequence[float], xy2: Sequence[float], slope: float, **kwargs
    ) -> None: ...
    def get_transform(self): ...
    def draw(self, renderer: RendererAgg) -> None: ...

class VertexSelector:
    def __init__(self, line: Line2D) -> None: ...
    def process_selected(self, ind: Sequence[int], xs: ArrayLike, ys: ArrayLike): ...
    def onpick(self, event: Event): ...

lineStyles = ...
lineMarkers = ...
drawStyles = ...
fillStyles = ...
