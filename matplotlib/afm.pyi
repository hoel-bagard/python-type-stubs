# COMPLETE

from typing import (BinaryIO, List, Literal, NamedTuple, Optional, Tuple,
                    Union, overload)

class CharMetrics(NamedTuple):
    width: float
    name: str
    bbox: List[int]

class CompositePart(NamedTuple):
    name: str
    dx: float
    dy: float

class AFM:
    def __init__(self, fh: BinaryIO) -> None: ...

    @property
    def postscript_name(self) -> str: ...
    @property
    def family_name(self) -> str: ...

    def get_angle(self) -> float: ...

    @overload
    def get_bbox_char(self, c: str, isord: Literal[False] = ...) -> List[int]: ...
    @overload
    def get_bbox_char(self, c: int, isord: Literal[True] = ...) -> List[int]: ...
    @overload
    def get_bbox_char(self, c: Union[str, int], isord: bool = ...) -> List[int]: ...

    def get_capheight(self) -> float: ...

    def get_familyname(self) -> str: ...
    def get_fontname(self) -> str: ...
    def get_fullname(self) -> str: ...
    
    @overload
    def get_height_char(self, c: str, isord: Literal[False] = ...) -> int: ...
    @overload
    def get_height_char(self, c: int, isord: Literal[True] = ...) -> int: ...
    @overload
    def get_height_char(self, c: Union[str, int], isord: bool = ...) -> int: ...

    def get_horizontal_stem_width(self) -> float: ...

    def get_kern_dist(self, c1: Union[str, int], c2: Union[str, int]) -> float: ...
    def get_kern_dist_from_name(self, name1: str, name2: str) -> float: ...

    @overload
    def get_name_char(self, c: str, isord: Literal[False] = ...) -> str: ...
    @overload
    def get_name_char(self, c: int, isord: Literal[True] = ...) -> str: ...
    @overload
    def get_name_char(self, c: Union[str, int], isord: bool = ...) -> str: ...
    
    def get_str_bbox(self, s: Union[str, bytes]) -> Tuple[float, float, float, float, float]: ...
    def get_str_bbox_and_descent(self, s: Union[str, bytes]) -> Tuple[float, float, float, float, float]: ...
    def get_underline_thickness(self) -> float: ...
    def get_vertical_stem_width(self) -> Optional[float]: ...
    def get_weight(self) -> str: ...

    @overload
    def get_width_char(self, c: str, isord: Literal[False] = ...) -> float: ...
    @overload
    def get_width_char(self, c: int, isord: Literal[True] = ...) -> float: ...
    @overload
    def get_width_char(self, c: Union[str, int], isord: bool = ...) -> float: ...

    def get_width_from_char_name(self, name: str) -> float: ...

    def get_xheight(self) -> float: ...

    def string_width_height(self, s: str) -> Tuple[float, float]: ...
