from matplotlib._enums import CapStyle, JoinStyle
from matplotlib.backend_bases import _Backend, FigureCanvasBase, FigureManagerBase, GraphicsContextBase, RendererBase

backend_version = ...


class RendererCairo(RendererBase):
    def __init__(self, dpi) -> None: ...
    def set_context(self, ctx)-> None: ...
    def set_ctx_from_surface(self, surface)-> None: ...
    def set_width_height(self, width, height)-> None: ...
    def draw_path(self, gc, path, transform, rgbFace=...)-> None: ...
    def draw_markers(
        self, gc, marker_path, marker_trans, path, transform, rgbFace=...
    )-> None: ...
    def draw_image(self, gc, x, y, im)-> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath=..., mtext=...)-> None: ...
    def get_canvas_width_height(self)-> tuple[float, float]: ...
    def get_text_width_height_descent(self, s, prop, ismath)-> tuple[float, float, float]: ...
    def new_gc(self)-> GraphicsContextCairo: ...
    def points_to_pixels(self, points)-> float: ...

class GraphicsContextCairo(GraphicsContextBase):
    def __init__(self, renderer) -> None: ...
    def restore(self)-> None: ...
    def set_alpha(self, alpha: float)-> None: ...
    def set_antialiased(self, b: bool) -> None: ...
    def set_capstyle(self, cs: CapStyle) -> None: ...
    def set_clip_rectangle(self, rectangle) -> None: ...
    def set_clip_path(self, path) -> None: ...
    def set_dashes(self, offset, dashes)-> None: ...
    def set_foreground(self, fg, isRGBA: bool|None=None) -> None: ...
    def get_rgb(self) -> tuple[float, float, float]: ...
    def set_joinstyle(self, js: JoinStyle) -> None: ...
    def set_linewidth(self, w: float)-> None: ...

class _CairoRegion:
    def __init__(self, slices, data) -> None: ...

class FigureCanvasCairo(FigureCanvasBase):
    def copy_from_bbox(self, bbox) -> _CairoRegion: ...
    def restore_region(self, region) -> None: ...
    def print_png(self, fobj)-> None: ...
    def print_rgba(self, fobj) -> None: ...

    print_raw = print_rgba
    def print_pdf(self, fobj, *, orientation='portrait') -> None: ...
    def print_ps(self, fobj, *, orientation='portrait') -> None: ...
    def print_svg(self, fobj, *, orientation='portrait') -> None: ...
    def print_svgz(self, fobj, *, orientation='portrait') -> None: ...

class _BackendCairo(_Backend):
    FigureCanvas = FigureCanvasCairo
    FigureManager = FigureManagerBase
