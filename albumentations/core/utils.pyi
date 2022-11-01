"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Sequence, Tuple

from .serialization import Serializable

def get_shape(img: Any) -> Tuple[int, int]:
    ...

def format_args(args_dict: Dict): # -> LiteralString:
    ...

class Params(Serializable, ABC):
    def __init__(self, format: str, label_fields: Optional[Sequence[str]] = ...) -> None:
        ...
    


class DataProcessor(ABC):
    def __init__(self, params: Params, additional_targets: Optional[Dict[str, str]] = ...) -> None:
        ...
    
    @property
    @abstractmethod
    def default_data_name(self) -> str:
        ...
    
    def ensure_data_valid(self, data: Dict[str, Any]) -> None:
        ...
    
    def ensure_transforms_valid(self, transforms: Sequence[object]) -> None:
        ...
    
    def postprocess(self, data: Dict[str, Any]) -> Dict[str, Any]:
        ...
    
    def preprocess(self, data: Dict[str, Any]) -> None:
        ...
    
    def check_and_convert(self, data: Sequence, rows: int, cols: int, direction: str = ...) -> Sequence:
        ...
    
    @abstractmethod
    def filter(self, data: Sequence, rows: int, cols: int) -> Sequence:
        ...
    
    @abstractmethod
    def check(self, data: Sequence, rows: int, cols: int) -> None:
        ...
    
    @abstractmethod
    def convert_to_albumentations(self, data: Sequence, rows: int, cols: int) -> Sequence:
        ...
    
    @abstractmethod
    def convert_from_albumentations(self, data: Sequence, rows: int, cols: int) -> Sequence:
        ...
    
    def add_label_fields_to_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        ...
    
    def remove_label_fields_from_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        ...
    


