from collections import OrderedDict
from collections.abc import MutableMapping
from functools import partial
from typing import Sequence

from ._typing import *
from .artist import allow_rasterization
from .axes import Axes
from .axis import Axis, XAxis, YAxis
from .backend_bases import RendererBase
from .patches import Patch
from .path import Path
from .transforms import Transform


class Spine(Patch):
    def __str__(self) -> str: ...
    def __init__(self, axes: Axes, spine_type: str, path: Path, **kwargs) -> None: ...
    def set_patch_arc(
        self, center: Sequence[float], radius: float, theta1: float, theta2: float
    ) -> None: ...
    def set_patch_circle(self, center: Sequence[float], radius: float) -> None: ...
    def set_patch_line(self): ...
    def get_patch_transform(self): ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def get_path(self): ...
    def register_axis(self, axis: Axis) -> None: ...
    def clear(self) -> None: ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def set_position(self, position: tuple[str, float]) -> None: ...
    def get_position(self) -> tuple[str, float]: ...
    def get_spine_transform(self) -> Transform: ...
    def set_bounds(self, low: float | None = ..., high: float | None = ...) -> None: ...
    def get_bounds(self): ...
    @classmethod
    def linear_spine(cls, axes, spine_type, **kwargs) -> Spine: ...
    @classmethod
    def arc_spine(
        cls,
        axes,
        spine_type,
        center: Sequence[float],
        radius: float,
        theta1: float,
        theta2: float,
        **kwargs
    ) -> Spine: ...
    @classmethod
    def circular_spine(cls, axes, center, radius, **kwargs): ...
    def set_color(self, c: Color) -> None: ...

class SpinesProxy:
    def __init__(self, spine_dict: dict[str, Spine]) -> None: ...
    def __getattr__(self, name: str) -> partial: ...
    def __dir__(self): ...

class Spines(MutableMapping):
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def from_dict(cls, d: OrderedDict | dict[str, Spine]) -> "Spines": ...
    def __getstate__(self): ...
    def __setstate__(self, state): ...
    def __getattr__(self, name: str) -> Spine: ...
    def __getitem__(self, key: list[str] | slice | str) -> Spine: ...
    def __setitem__(self, key: str, value: Spine) -> None: ...
    def __delitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
