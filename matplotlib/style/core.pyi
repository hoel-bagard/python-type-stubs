import contextlib
from typing import Generator


__all__ = ["use", "context", "available", "library", "reload_library"]

class __getattr__:
    STYLE_FILE_PATTERN = ...

BASE_LIBRARY_PATH: str = ...
USER_LIBRARY_PATHS: list[str] = ...
STYLE_EXTENSION: str = ...
STYLE_BLACKLIST: set[str] = ...

def use(style: str) -> None: ...
@contextlib.contextmanager
def context(style: str, after_reset: bool = ...)-> Generator: ...
def load_base_library() -> dict: ...
def iter_user_libraries()-> Generator: ...
def update_user_library(library): ...
def read_style_directory(
    style_dir: str,
) -> dict: ...
def update_nested_dict(main_dict: dict, new_dict: dict): ...

library = ...
available: list = ...

def reload_library() -> None: ...
