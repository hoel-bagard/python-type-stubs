from typing import Any, Callable, Literal, Sequence

from ._typing import *
from .artist import Artist
from .backend_bases import Event, MouseEvent, RendererBase
from .colors import Colormap, Normalize
from .figure import Figure
from .font_manager import FontProperties
from .patches import FancyBboxPatch
from .text import _AnnotationBase
from .transforms import Bbox, BboxBase, Transform


DEBUG = ...

def bbox_artist(*args, **kwargs): ...

class OffsetBox(Artist):
    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, fig: Figure): ...
    def axes(self, ax): ...
    def contains(self, mouseevent: MouseEvent) -> tuple[bool, dict]: ...
    def set_offset(self, xy: Callable): ...
    def get_offset(
        self, width, height, xdescent, ydescent, renderer: RendererBase
    ) -> tuple[float, float]: ...
    def set_width(self, width: float): ...
    def set_height(self, height: float): ...
    def get_visible_children(self) -> list[Artist]: ...
    def get_children(self) -> list[Artist]: ...
    def get_extent_offsets(
        self, renderer: RendererBase
    ) -> tuple[float, float, float, float, list[tuple[float, float]]]: ...
    def get_extent(
        self, renderer: RendererBase
    ) -> tuple[float, float, float, float]: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def draw(self, renderer: RendererBase): ...

class PackerBase(OffsetBox):
    def __init__(
        self,
        pad: float = ...,
        sep: float = ...,
        width: float = ...,
        height: float = ...,
        align: Literal[
            "top", "bottom", "left", "right", "center", "baseline"
        ] = "baseline",
        mode: Literal["fixed", "expand", "equal"] = "fixed",
        children: list[Artist] = ...,
    ) -> None: ...

class VPacker(PackerBase):
    def get_extent_offsets(self, renderer: RendererBase) -> list: ...

class HPacker(PackerBase):
    def get_extent_offsets(self, renderer: RendererBase) -> list: ...

class PaddedBox(OffsetBox):
    def __init__(
        self,
        child: Artist,
        pad: float = ...,
        draw_frame: bool = ...,
        patch_attrs: dict | None = ...,
    ) -> None: ...
    def get_extent_offsets(self, renderer: RendererBase) -> list: ...
    def draw(self, renderer: RendererBase): ...
    def update_frame(self, bbox: Bbox, fontsize: float = ...): ...
    def draw_frame(self, renderer: RendererBase): ...

class DrawingArea(OffsetBox):
    def __init__(
        self,
        width: float,
        height: float,
        xdescent: float = ...,
        ydescent: float = ...,
        clip: bool = ...,
    ) -> None: ...
    @property
    def clip_children(self): ...
    @clip_children.setter
    def clip_children(self, val): ...
    def get_transform(self) -> Transform: ...
    def set_transform(self, t) -> None: ...
    def set_offset(self, xy: Sequence[float]) -> None: ...
    def get_offset(self) -> tuple[float, float]: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def add_artist(self, a: Artist): ...
    def draw(self, renderer: RendererBase): ...

class TextArea(OffsetBox):
    def __init__(
        self, s: str, textprops: dict = ..., multilinebaseline: bool = False
    ) -> None: ...
    def set_text(self, s: str): ...
    def get_text(self) -> str: ...
    def set_multilinebaseline(self, t: bool): ...
    def get_multilinebaseline(self) -> bool: ...
    def set_transform(self, t: Transform) -> None: ...
    def set_offset(self, xy: Sequence[float]) -> None: ...
    def get_offset(self) -> tuple[float, float]: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AuxTransformBox(OffsetBox):
    def __init__(self, aux_transform) -> None: ...
    def add_artist(self, a: Artist): ...
    def get_transform(self) -> Transform: ...
    def set_transform(self, t: Transform): ...
    def set_offset(self, xy: Sequence[float]): ...
    def get_offset(self) -> tuple[float, float]: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AnchoredOffsetbox(OffsetBox):

    zorder = ...
    codes = ...

    def __init__(
        self,
        loc: str,
        pad: float = ...,
        borderpad: float = ...,
        child: OffsetBox = ...,
        prop: FontProperties = ...,
        frameon: bool = ...,
        bbox_to_anchor: BboxBase | Sequence[float] = ...,
        bbox_transform: Transform | None = ...,
        **kwargs
    ) -> None: ...
    def set_child(self, child): ...
    def get_child(self): ...
    def get_children(self) -> list: ...
    def get_extent(self, renderer: RendererBase): ...
    def get_bbox_to_anchor(self) -> Bbox: ...
    def set_bbox_to_anchor(self, bbox: Bbox, transform: Transform = ...): ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def update_frame(self, bbox: Bbox, fontsize: float = ...): ...
    def draw(self, renderer: RendererBase): ...

class AnchoredText(AnchoredOffsetbox):

    patch: FancyBboxPatch

    def __init__(
        self,
        s: str,
        loc: str,
        pad: float = ...,
        borderpad: float = ...,
        prop: dict = ...,
        **kwargs
    ) -> None: ...

class OffsetImage(OffsetBox):
    def __init__(
        self,
        arr,
        zoom: float = ...,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        dpi_cor=...,
        **kwargs
    ) -> None: ...
    def set_data(self, arr: ArrayLike): ...
    def get_data(self): ...
    def set_zoom(self, zoom: float): ...
    def get_zoom(self) -> float: ...
    def get_offset(self): ...
    def get_children(self): ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_extent(self, renderer: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class AnnotationBbox(Artist, _AnnotationBase):

    zorder = ...
    def __str__(self) -> str: ...
    def __init__(
        self,
        offsetbox,
        xy: Sequence[float],
        xybox: Sequence[float] = ...,
        xycoords: str | Artist | Transform | Callable | Sequence[float] = "data",
        boxcoords: str | Artist | Transform | Callable | Sequence[float] = ...,
        frameon: bool = True,
        pad: float = 0.4,
        annotation_clip=...,
        box_alignment: Sequence[float] = ...,
        bboxprops=...,
        arrowprops=...,
        fontsize: float = ...,
        **kwargs
    ) -> None: ...
    @property
    def xyann(self): ...
    @xyann.setter
    def xyann(self, xyann): ...
    @property
    def anncoords(self): ...
    @anncoords.setter
    def anncoords(self, coords): ...
    def contains(self, mouseevent: MouseEvent): ...
    def get_children(self) -> list: ...
    def set_figure(self, fig: Figure): ...
    def set_fontsize(self, s: float = ...): ...
    def get_fontsize(self) -> float: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_tightbbox(self, renderer: RendererBase = ...) -> Bbox: ...
    def update_positions(self, renderee: RendererBase): ...
    def draw(self, renderer: RendererBase): ...

class DraggableBase:
    def __init__(self, ref_artist, use_blit: bool = ...) -> None: ...
    def on_motion(self, evt: Event): ...
    def on_pick(self, evt: Event): ...
    def on_release(self, event: Event): ...
    def disconnect(self): ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
    def finalize_offset(self): ...

class DraggableOffsetBox(DraggableBase):
    def __init__(self, ref_artist, offsetbox, use_blit: bool = ...) -> None: ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
    def get_loc_in_canvas(self): ...

class DraggableAnnotation(DraggableBase):
    def __init__(self, annotation, use_blit: bool = ...) -> None: ...
    def save_offset(self): ...
    def update_offset(self, dx: float, dy: float): ...
