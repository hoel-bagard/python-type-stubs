from typing import Callable, Literal

import numpy as np
from matplotlib._typing import *
from matplotlib.axes._base import _AxesBase
from matplotlib.transforms import Transform


class SecondaryAxis(_AxesBase):
    def __init__(self, parent, orientation, location, functions, **kwargs) -> None: ...
    def set_alignment(
        self, align: Literal["top", "bottom", "left", "right"]
    ) -> None: ...
    def set_location(
        self, location: Literal["top", "bottom", "left", "right"] | float
    ) -> None: ...
    def apply_aspect(self, position=None) -> None: ...
    def set_ticks(
        self,
        ticks: list[float],
        labels: list[str]|None = None,
        *,
        minor: bool = False,
        **kwargs
    ) -> list: ...
    def set_functions(
        self, functions: tuple[Callable, Callable] | Transform
    ) -> None: ...
    def draw(self, *args, **kwargs) -> None: ...
    def set_aspect(self, *args, **kwargs) -> None: ...
    def set_color(self, color: Color) -> None: ...
