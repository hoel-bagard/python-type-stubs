from typing import Callable

from matplotlib.widgets import LockDraw

from .backend_bases import Event, FigureCanvasBase
from .backend_tools import ToolBase
from .figure import Figure

class ToolEvent:
    def __init__(self, name: str, sender, tool, data=...) -> None: ...

class ToolTriggerEvent(ToolEvent):
    def __init__(self, name: str, sender, tool, canvasevent=..., data=...) -> None: ...

class ToolManagerMessageEvent:
    def __init__(self, name: str, sender, message) -> None: ...

class ToolManager:

    keypresslock: LockDraw
    messagelock: LockDraw

    def __init__(self, figure=...) -> None: ...
    @property
    def canvas(self) -> FigureCanvasBase: ...
    @property
    def figure(self) -> Figure: ...
    @figure.setter
    def figure(self, figure: Figure) -> None: ...
    def set_figure(self, figure: Figure, update_tools: bool = ...)-> None: ...
    def toolmanager_connect(self, s: str, func: Callable) -> int: ...
    def toolmanager_disconnect(self, cid: int): ...
    def message_event(self, message, sender=...)-> None: ...
    @property
    def active_toggle(self)-> dict: ...
    def get_tool_keymap(self, name: str) -> list[str]: ...
    def update_keymap(self, name: str, key: list[str] | str) -> None: ...
    def remove_tool(self, name: str) -> None: ...
    def add_tool(self, name: str, tool: type, *args, **kwargs)-> ToolBase: ...
    def trigger_tool(
        self,
        name: str,
        sender: object = ...,
        canvasevent: Event = ...,
        data: object = ...,
    )-> None: ...
    @property
    def tools(self)-> dict[str, ToolBase]: ...
    def get_tool(
        self, name: str | ToolBase, warn: bool = ...
    ) -> tuple[ToolBase, None]: ...
