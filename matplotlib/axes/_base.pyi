from typing import (Any, Callable, Collection, Literal, MutableSequence,
                    Sequence, overload)

import numpy as np
from matplotlib._typing import *
from matplotlib.artist import Artist, allow_rasterization
from matplotlib.axis import XAxis, YAxis
from matplotlib.backend_bases import MouseButton, MouseEvent, RendererBase
from matplotlib.cbook import Grouper
from matplotlib.container import Container
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.scale import ScaleBase
from matplotlib.table import Table
from matplotlib.transforms import Bbox, BboxBase, Transform, TransformedBbox

from ._axes import Axes

class _axis_method_wrapper:
    def __init__(self, attr_name, method_name, *, doc_sub=...) -> None: ...
    def __set_name__(self, owner, name) -> None: ...

class _AxesBase(Artist):
    name: str = ...

    def __str__(self) -> str: ...
    def __init__(
        self,
        fig: Figure,
        rect: Sequence[float],
        *,
        facecolor: Color|None=None,
        frameon: bool = True,
        sharex: Axes|None = None,
        sharey: Axes|None = None,
        label: str='',
        xscale: float|None=None,
        yscale: float|None=None,
        box_aspect: float|None = None,
        **kwargs
    ) -> None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, state)-> None: ...
    def __repr__(self)-> str: ...
    def get_window_extent(self, renderer=..., *args, **kwargs) -> TransformedBbox: ...
    def set_figure(self, fig: Figure)-> None: ...
    @property
    def viewLim(self)-> Bbox: ...
    def get_xaxis_transform(self, which=...) -> Transform: ...
    def get_xaxis_text1_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_xaxis_text2_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_yaxis_transform(self, which=...) -> Transform: ...
    def get_yaxis_text1_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_yaxis_text2_transform(self, pad_points) -> tuple[Transform, str, str]: ...
    def get_position(self, original: bool = ...) -> Bbox: ...
    def set_position(
        self,
        pos: Sequence[float] | Bbox,
        which: Literal["both", "active", "original"] = ...,
    ) -> None: ...
    def reset_position(self) -> None: ...
    def set_axes_locator(
        self, locator: Callable[[Axes, RendererBase], Bbox]
    ) -> None: ...
    def get_axes_locator(self) -> Callable[[Axes, RendererBase], Bbox]: ...
    def sharex(self, other: Axes) -> None: ...
    def sharey(self, other: Axes) -> None: ...
    def clear(self) -> None: ...
    @property
    def artists(self) -> MutableSequence: ...
    def collections(self): ...
    @property
    def images(self)-> MutableSequence: ...
    @property
    def lines(self)-> MutableSequence: ...
    @property
    def patches(self)-> MutableSequence: ...
    @property
    def tables(self)-> MutableSequence: ...
    @property
    def texts(self)-> MutableSequence: ...
    def cla(self) -> None: ...
    def get_facecolor(self) -> Color: ...
    def set_facecolor(self, color: Color)-> None: ...
    def set_prop_cycle(self, *args, **kwargs)-> None: ...
    def get_aspect(self) -> Literal["auto"] | float: ...
    def set_aspect(
        self,
        aspect: Literal["auto", "equal"] | float,
        adjustable: None | Literal["box", "datalim"] = ...,
        anchor: None | str | Sequence[float] = ...,
        share: bool = False,
    )-> None: ...
    def get_adjustable(self) -> str: ...
    def set_adjustable(
        self, adjustable: Literal["box", "datalim"], share: bool = False
    )-> None: ...
    def get_box_aspect(self) -> float | None: ...
    def set_box_aspect(self, aspect: float | None = ...) -> None: ...
    def get_anchor(self) -> str: ...
    def set_anchor(
        self,
        anchor: Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        share: bool = False,
    )-> None: ...
    def get_data_ratio(self)-> float: ...
    def apply_aspect(self, position=...)-> None: ...
    def axis(self, *args, emit: bool = ..., **kwargs)-> tuple[float, float, float, float]: ...
    def get_legend(self) -> Legend | None: ...
    def get_images(self) -> list[AxesImage]: ...
    def get_lines(self) -> list[Line2D]: ...
    def get_xaxis(self) -> XAxis: ...
    def get_yaxis(self) -> YAxis: ...
    get_xgridlines = ...
    get_xticklines = ...
    get_ygridlines = ...
    get_yticklines = ...
    def has_data(self) -> bool: ...
    def add_artist(self, a: Artist) -> Artist: ...
    def add_child_axes(self, ax: _AxesBase) -> Axes: ...
    def add_collection(self, collection: Collection, autolim=...) -> Collection: ...
    def add_image(self, image: AxesImage) -> AxesImage: ...
    def add_line(self, line: Line2D) -> Line2D: ...
    def add_patch(self, p: Patch) -> Patch: ...
    def add_table(self, tab: Table) -> Table: ...
    def add_container(self, container: Container) -> Container: ...
    def relim(self, visible_only: bool = ...)-> None: ...
    def update_datalim(self, xys, updatex: bool = ..., updatey: bool = ...)-> None: ...
    def in_axes(self, mouseevent) -> bool: ...
    get_autoscalex_on = ...
    get_autoscaley_on = ...
    set_autoscalex_on = ...
    set_autoscaley_on = ...
    def get_autoscale_on(self) -> bool: ...
    def set_autoscale_on(self, b: bool)-> None: ...
    @property
    def use_sticky_edges(self) -> bool: ...
    @use_sticky_edges.setter
    def use_sticky_edges(self, b: bool)-> None: ...
    def set_xmargin(self, m: float)-> None: ...
    def set_ymargin(self, m: float)-> None: ...
    def margins(
        self, *margins, x: float = ..., y: float = ..., tight: bool | None = True
    ) -> tuple[float, float]: ...
    def set_rasterization_zorder(self, z: float | None) -> None: ...
    def get_rasterization_zorder(self) -> float: ...
    def autoscale(
        self,
        enable: bool | None = ...,
        axis: Literal["both", "x", "y"] = ...,
        tight: bool | None = ...,
    ) -> None: ...
    def autoscale_view(
        self, tight: bool | None = ..., scalex: bool = True, scaley: bool = True
    ) -> None: ...
    @allow_rasterization
    def draw(self, renderer)-> None: ...
    def draw_artist(self, a: Artist) -> None: ...
    def redraw_in_frame(self) -> None: ...
    def get_renderer_cache(self): ...
    def get_frame_on(self) -> bool: ...
    def set_frame_on(self, b: bool) -> None: ...
    def get_axisbelow(self) -> tuple[bool, Literal["line"]]: ...
    def set_axisbelow(self, b: bool | Literal["line"]) -> None: ...
    def grid(
        self,
        visible: bool | None = ...,
        which: Literal["major", "minor", "both"] = ...,
        axis: Literal["both", "x", "y"] = ...,
        **kwargs
    ) -> None: ...
    def ticklabel_format(
        self,
        *,
        axis: Literal["x", "y", "both"] = ...,
        style: Literal["sci", "scientific", "plain"] = ...,
        scilimits=...,
        useOffset: bool | float = ...,
        useLocale: bool = ...,
        useMathText: bool = ...
    )-> None: ...
    def locator_params(
        self, axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
    ) -> None: ...
    def tick_params(self, axis: Literal["x", "y", "both"] = ..., **kwargs) -> None: ...
    def set_axis_off(self) -> None: ...
    def set_axis_on(self) -> None: ...
    def get_xlabel(self) -> str: ...
    def set_xlabel(
        self,
        xlabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["left", "center", "right"] = ...,
        **kwargs
    )-> None: ...
    def invert_xaxis(self) -> None: ...
    xaxis_inverted = ...
    def get_xbound(self) -> tuple[float, float]: ...
    def set_xbound(
        self, lower: float | None = ..., upper: float | None = ...
    ) -> None: ...
    def get_xlim(self) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: tuple[float | np.datetime64, float | np.datetime64],
        *,
        emit: bool = ...,
        auto: bool | None = ...,
        xmin: float = ...,
        xmax: float = ...
    ) -> tuple[float, float]: ...
    @overload
    def set_xlim(
        self,
        left: float | np.datetime64 = ...,
        right: float | np.datetime64 = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        xmin: float = ...,
        xmax: float = ...
    ) -> tuple[float, float]: ...
    def get_xscale(self) -> str: ...
    def set_xscale(
        self, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    )-> None: ...
    get_xticks = ...
    set_xticks = ...
    get_xmajorticklabels = ...
    get_xminorticklabels = ...
    get_xticklabels = ...
    set_xticklabels = ...
    def get_ylabel(self) -> str: ...
    def set_ylabel(
        self,
        ylabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["bottom", "center", "top"] = ...,
        **kwargs
    ) -> None: ...
    def invert_yaxis(self) -> None: ...
    yaxis_inverted = ...
    def get_ybound(self) -> tuple[float, float]: ...
    def set_ybound(
        self, lower: float | None = ..., upper: float | None = ...
    ) -> None: ...
    def get_ylim(self) -> tuple[float, float]: ...
    def set_ylim(
        self,
        bottom: float = ...,
        top: float = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        ymin: float = ...,
        ymax: float = ...
    )-> None: ...
    get_yscale = ...
    def set_yscale(
        self, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    ) -> None: ...
    get_yticks = ...
    set_yticks = ...
    get_ymajorticklabels = ...
    get_yminorticklabels = ...
    get_yticklabels = ...
    set_yticklabels = ...
    xaxis_date = ...
    yaxis_date = ...
    def format_xdata(self, x) -> str: ...
    def format_ydata(self, y) -> str: ...
    def format_coord(self, x, y) -> str: ...
    def minorticks_on(self) -> None: ...
    def minorticks_off(self) -> None: ...
    def can_zoom(self) -> bool: ...
    def can_pan(self) -> bool: ...
    def get_navigate(self) -> bool: ...
    def set_navigate(self, b: bool) -> None: ...
    def get_navigate_mode(self) -> str | None: ...
    def set_navigate_mode(self, b: str | None) -> None: ...
    def start_pan(self, x: float, y: float, button: MouseButton) -> None: ...
    def end_pan(self) -> None: ...
    def drag_pan(
        self, button: MouseButton, key: str | None, x: float, y: float
    ) -> None: ...
    def get_children(self)-> list: ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def contains_point(self, point) -> bool: ...
    def get_default_bbox_extra_artists(self) -> list[Artist]: ...
    def get_tightbbox(
        self,
        renderer: RendererBase = ...,
        call_axes_locator: bool = ...,
        bbox_extra_artists: list | None = ...,
        *,
        for_layout_only=...
    ) -> BboxBase: ...
    def twinx(self) -> Axes: ...
    def twiny(self) -> Axes: ...
    def get_shared_x_axes(self) -> Grouper: ...
    def get_shared_y_axes(self) -> Grouper: ...
