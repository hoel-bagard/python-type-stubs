from typing import Literal, Sequence

import numpy as np

from ._enums import CapStyle, JoinStyle
from ._typing import *
from .artist import Artist, allow_rasterization
from .backend_bases import MouseEvent, RendererBase
from .path import Path
from .transforms import Bbox, Transform

class Patch(Artist):

    zorder: float = ...

    def __init__(
        self,
        edgecolor: Color = ...,
        facecolor: Color = ...,
        color: Color = ...,
        linewidth: float = ...,
        linestyle=...,
        antialiased: bool = ...,
        hatch=...,
        fill=...,
        capstyle: CapStyle = ...,
        joinstyle: JoinStyle = ...,
        **kwargs
    ) -> None: ...
    def get_verts(self): ...
    def contains(self, mouseevent: MouseEvent, radius: float = ...): ...
    def contains_point(self, point: Sequence[float], radius: float = ...) -> bool: ...
    def contains_points(self, points: ArrayLike, radius: float = ...) -> list[bool]: ...
    def update_from(self, other: Patch): ...
    def get_extents(self) -> Bbox: ...
    def get_transform(self) -> Transform: ...
    def get_data_transform(self) -> Transform: ...
    def get_patch_transform(self) -> Transform: ...
    def get_antialiased(self) -> bool: ...
    def get_edgecolor(self) -> Color: ...
    def get_facecolor(self) -> Color: ...
    def get_linewidth(self) -> float: ...
    def get_linestyle(self): ...
    def set_antialiased(self, aa: bool | None): ...
    def set_edgecolor(self, color: Color | None): ...
    def set_facecolor(self, color: Color | None): ...
    def set_color(self, c: Color): ...
    def set_alpha(self, alpha: Scalar | None): ...
    def set_linewidth(self, w: float | None): ...
    def set_linestyle(
        self,
        ls: Literal[
            "-",
            "solid",
            "--",
            "dashed",
            "-.",
            "dashdot",
            ":",
            "dotted",
            "None",
            "none",
            " ",
            "",
        ],
    ): ...
    def set_fill(self, b: bool): ...
    def get_fill(self) -> bool: ...
    fill = ...

    def set_capstyle(self, s: CapStyle | Literal["butt", "projecting", "round"]): ...
    def get_capstyle(self) -> CapStyle: ...
    def set_joinstyle(self, s: JoinStyle | Literal["miter", "round", "bevel"]): ...
    def get_joinstyle(self) -> JoinStyle | str: ...
    def set_hatch(
        self, hatch: Literal["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]
    ): ...
    def get_hatch(self) -> str: ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def get_path(self) -> Path: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...

class Shadow(Patch):
    def __str__(self) -> str: ...
    def __init__(self, patch: Patch, ox: float, oy: float, **kwargs) -> None: ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...
    def draw(self, renderer: RendererBase): ...

class Rectangle(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        *,
        rotation_point: Literal["xy", "center"] | Sequence[float] = "xy",
        **kwargs
    ) -> None: ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self): ...
    @property
    def rotation_point(self): ...
    @rotation_point.setter
    def rotation_point(self, value): ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_xy(self) -> tuple[float, float]: ...
    def get_corners(self) -> list[tuple[float, float]]: ...
    def get_center(self) -> tuple[float, float]: ...
    def get_width(self) -> float: ...
    def get_height(self) -> float: ...
    def get_angle(self) -> float: ...
    def set_x(self, x: float): ...
    def set_y(self, y: float): ...
    def set_angle(self, angle: float): ...
    def set_xy(self, xy: Sequence[float]): ...
    def set_width(self, w: float): ...
    def set_height(self, h: float): ...
    def set_bounds(self, *args): ...
    def get_bbox(self) -> Bbox: ...
    xy: tuple[float, float] = ...

class RegularPolygon(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        numVertices: int,
        radius: float = ...,
        orientation: float = ...,
        **kwargs
    ) -> None: ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...

class PathPatch(Patch):
    def __str__(self) -> str: ...
    def __init__(self, path: Path, **kwargs) -> None: ...
    def get_path(self) -> Path: ...
    def set_path(self, path: Path): ...

class StepPatch(PathPatch):
    def __init__(
        self,
        values: ArrayLike,
        edges: ArrayLike,
        *,
        orientation: Literal["vertical", "horizontal"] = "vertical",
        baseline: float | ArrayLike | None = 0,
        **kwargs
    ) -> None: ...
    def get_data(self): ...
    def set_data(
        self,
        values: ArrayLike | None = ...,
        edges: ArrayLike = ...,
        baseline: float | ArrayLike | None = ...,
    ): ...

class Polygon(Patch):
    def __str__(self) -> str: ...
    def __init__(self, xy: Sequence[float], closed: bool = ..., **kwargs) -> None: ...
    def get_path(self) -> Path: ...
    def get_closed(self) -> bool: ...
    def set_closed(self, closed: bool): ...
    def get_xy(self) -> np.ndarray: ...
    def set_xy(self, xy: ArrayLike): ...
    xy = ...

class Wedge(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        center: Sequence[float],
        r: float,
        theta1: float,
        theta2: float,
        width: float = ...,
        **kwargs
    ) -> None: ...
    def set_center(self, center: Sequence[float]): ...
    def set_radius(self, radius: float): ...
    def set_theta1(self, theta1: float): ...
    def set_theta2(self, theta2: float): ...
    def set_width(self, widt: float): ...
    def get_path(self) -> Path: ...

class Arrow(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self, x: float, y: float, dx: float, dy: float, width: float = ..., **kwargs
    ) -> None: ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...

class FancyArrow(Polygon):
    def __str__(self) -> str: ...
    def __init__(
        self,
        x: float,
        y: float,
        dx: float,
        dy: float,
        width: float = 0.001,
        length_includes_head: bool = False,
        head_width: float = ...,
        head_length: float | None = ...,
        shape: Literal["full", "left", "right"] = "full",
        overhang: float = 0,
        head_starts_at_zero: bool = False,
        **kwargs
    ) -> None: ...
    def set_data(
        self,
        *,
        x: float | None = None,
        y: float | None = None,
        dx: float | None = None,
        dy: float | None = None,
        width: float | None = None,
        head_width: float | None = None,
        head_length: float | None = None
    ): ...

class CirclePolygon(RegularPolygon):
    def __str__(self) -> str: ...
    def __init__(
        self, xy: Sequence[float], radius: float = ..., resolution=..., **kwargs
    ) -> None: ...

class Ellipse(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        **kwargs
    ) -> None: ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...
    def set_center(self, xy: Sequence[float]): ...
    def get_center(self) -> tuple[float, float]: ...
    center = ...
    def set_width(self, width: float): ...
    def get_width(self) -> float: ...
    width = ...
    def set_height(self, height: float): ...
    def get_height(self) -> float: ...
    height = ...
    def set_angle(self, angle: float): ...
    def get_angle(self) -> float: ...
    angle = ...
    def get_corners(self): ...

class Annulus(Patch):
    def __init__(
        self,
        xy: Sequence[float],
        r: float | Sequence[float],
        width: float,
        angle: float = 0,
        **kwargs
    ) -> None: ...
    def __str__(self) -> str: ...
    def set_center(self, xy: Sequence[float]): ...
    def get_center(self) -> tuple[float, float]: ...
    center = ...
    def set_width(self, width: float): ...
    def get_width(self) -> float: ...
    width = ...
    def set_angle(self, angle: float): ...
    def get_angle(self) -> float: ...
    angle = ...
    def set_semimajor(self, a: float): ...
    def set_semiminor(self, b: float): ...
    def set_radii(self, r: float): ...
    def get_radii(self) -> float: ...
    radii = ...
    def get_path(self) -> Path: ...

class Circle(Ellipse):
    def __str__(self) -> str: ...
    def __init__(self, xy: Sequence[float], radius: float = ..., **kwargs) -> None: ...
    def set_radius(self, radius: float): ...
    def get_radius(self) -> float: ...
    radius: float = ...

class Arc(Ellipse):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        theta1: float = 0,
        theta2: float = 360,
        **kwargs
    ) -> None: ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...

def bbox_artist(artist, renderer: RendererBase, props: dict = ..., fill=...): ...
def draw_bbox(
    bbox, renderer: RendererBase, color: Color = ..., trans: Transform = ...
): ...

class _Style:
    def __new__(cls, stylename: str, **kwargs): ...
    @classmethod
    def get_styles(cls): ...
    @classmethod
    def pprint_styles(cls): ...
    @classmethod
    def register(cls, name: str, style: _Style): ...

class BoxStyle(_Style):
    class Square:
        def __init__(self, pad: float = 0.3) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Circle:
        def __init__(self, pad: float = 0.3) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class LArrow:
        def __init__(self, pad: float = 0.3) -> None: ...
        def __call__(self, x0, y0, width, height, mutation_size): ...

    class RArrow(LArrow):
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class DArrow:
        def __init__(self, pad: float = 0.3) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Round:
        def __init__(self, pad=0.3, rounding_size: float = ...) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Round4:
        def __init__(self, pad: float = 0.3, rounding_size: float = ...) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Sawtooth:
        def __init__(self, pad: float = 0.3, tooth_size: float = ...) -> None: ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Roundtooth(Sawtooth):
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

class ConnectionStyle(_Style):
    class _Base:
        class SimpleEvent:
            def __init__(self, xy: Sequence[float]) -> None: ...

        def __call__(
            self, posA, posB, shrinkA=..., shrinkB=..., patchA=..., patchB=...
        ): ...

    class Arc3(_Base):
        def __init__(self, rad=...) -> None: ...
        def connect(self, posA, posB): ...

    class Angle3(_Base):
        def __init__(self, angleA: float = ..., angleB: float = ...) -> None: ...
        def connect(self, posA, posB): ...

    class Angle(_Base):
        def __init__(
            self, angleA: float = ..., angleB: float = ..., rad: float = ...
        ) -> None: ...
        def connect(self, posA, posB): ...

    class Arc(_Base):
        def __init__(
            self,
            angleA: float = ...,
            angleB: float = ...,
            armA: float = ...,
            armB: float = ...,
            rad: float = ...,
        ) -> None: ...
        def connect(self, posA, posB): ...

    class Bar(_Base):
        def __init__(
            self,
            armA: float = ...,
            armB: float = ...,
            fraction: float = ...,
            angle: float = ...,
        ) -> None: ...
        def connect(self, posA, posB): ...

class ArrowStyle(_Style):
    class _Base:
        @staticmethod
        def ensure_quadratic_bezier(path: Path): ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...
        def __call__(
            self, path: Path, mutation_size, linewidth: float, aspect_ratio: float = ...
        ): ...

    class _Curve(_Base):

        beginarrow = ...
        arrow = ...
        fillbegin = ...
        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            widthA: float = ...,
            widthB: float = ...,
            lengthA: float = ...,
            lengthB: float = ...,
            angleA: float = ...,
            angleB: float = ...,
            scaleA: float = ...,
            scaleB: float = ...,
        ) -> None: ...
        def transmute(self, path, mutation_size, linewidth): ...

    class Curve(_Curve):
        def __init__(self) -> None: ...

    class CurveA(_Curve):

        arrow = ...

    class CurveB(_Curve):

        arrow = ...

    class CurveAB(_Curve):

        arrow = ...

    class CurveFilledA(_Curve):

        arrow = ...

    class CurveFilledB(_Curve):

        arrow = ...

    class CurveFilledAB(_Curve):

        arrow = ...

    class BracketA(_Curve):

        arrow = ...
        def __init__(
            self, widthA: float = ..., lengthA: float = ..., angleA: float = ...
        ) -> None: ...

    class BracketB(_Curve):

        arrow = ...
        def __init__(
            self, widthB: float = ..., lengthB: float = ..., angleB: float = ...
        ) -> None: ...

    class BracketAB(_Curve):

        arrow = ...
        def __init__(
            self,
            widthA: float = ...,
            lengthA: float = ...,
            angleA: float = ...,
            widthB: float = ...,
            lengthB: float = ...,
            angleB: float = ...,
        ) -> None: ...

    class BarAB(_Curve):

        arrow = ...
        def __init__(
            self,
            widthA: float = ...,
            angleA: float = ...,
            widthB: float = ...,
            angleB: float = ...,
        ) -> None: ...

    class BracketCurve(_Curve):

        arrow = ...
        def __init__(
            self, widthA: float = ..., lengthA: float = ..., angleA: float = ...
        ) -> None: ...

    class CurveBracket(_Curve):

        arrow = ...
        def __init__(
            self, widthB: float = ..., lengthB: float = ..., angleB: float = ...
        ) -> None: ...

    class Simple(_Base):
        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            tail_width: float = ...,
        ) -> None: ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

    class Fancy(_Base):
        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            tail_width: float = ...,
        ) -> None: ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

    class Wedge(_Base):
        def __init__(
            self, tail_width: float = ..., shrink_factor: float = ...
        ) -> None: ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

class FancyBboxPatch(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        boxstyle: str | BoxStyle = ...,
        bbox_transmuter=...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        **kwargs
    ) -> None: ...
    def set_boxstyle(self, boxstyle: str | BoxStyle = ..., **kwargs): ...
    def set_mutation_scale(self, scale: float): ...
    def get_mutation_scale(self): ...
    def set_mutation_aspect(self, aspect: float): ...
    def get_mutation_aspect(self) -> float: ...
    def get_boxstyle(self) -> str | BoxStyle: ...
    def get_path(self) -> Path: ...
    def get_x(self) -> float: ...
    def get_y(self) -> float: ...
    def get_width(self) -> float: ...
    def get_height(self) -> float: ...
    def set_x(self, x: float): ...
    def set_y(self, y: float): ...
    def set_width(self, w: float): ...
    def set_height(self, h: float): ...
    def set_bounds(self, *args): ...
    def get_bbox(self) -> Bbox: ...

class FancyArrowPatch(Patch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        posA: Sequence[float] = ...,
        posB: Sequence[float] = ...,
        path: Path = ...,
        arrowstyle: str | ArrowStyle = ...,
        connectionstyle: str | ConnectionStyle = ...,
        patchA: Patch = ...,
        patchB: Patch = ...,
        shrinkA: float = ...,
        shrinkB: float = ...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        **kwargs
    ) -> None: ...
    def set_positions(
        self, posA: None | Sequence[float], posB: None | Sequence[Sequence]
    ): ...
    def set_patchA(self, patchA: Patch): ...
    def set_patchB(self, patchB: Patch): ...
    def set_connectionstyle(
        self, connectionstyle: str | ConnectionStyle | None, **kwargs
    ): ...
    def get_connectionstyle(self) -> ConnectionStyle: ...
    def set_arrowstyle(self, arrowstyle: None | ArrowStyle | str = ..., **kwargs): ...
    def get_arrowstyle(self) -> ArrowStyle: ...
    def set_mutation_scale(self, scale: float): ...
    def get_mutation_scale(self) -> float: ...
    def set_mutation_aspect(self, aspect: float): ...
    def get_mutation_aspect(self) -> float: ...
    def get_path(self) -> Path: ...
    get_path_in_displaycoord = ...
    def draw(self, renderer: RendererBase): ...

class ConnectionPatch(FancyArrowPatch):
    def __str__(self) -> str: ...
    def __init__(
        self,
        xyA: Sequence[float],
        xyB: Sequence[float],
        coordsA,
        coordsB=...,
        axesA=...,
        axesB=...,
        arrowstyle: str | ArrowStyle = ...,
        connectionstyle: str | ConnectionStyle = ...,
        patchA: Patch = ...,
        patchB: Patch = ...,
        shrinkA: float = ...,
        shrinkB: float = ...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        clip_on: bool = ...,
        **kwargs
    ) -> None: ...
    def set_annotation_clip(self, b: bool | None): ...
    def get_annotation_clip(self) -> bool: ...
    def draw(self, renderer): ...
