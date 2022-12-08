"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List, Optional, Sequence, Tuple

from .utils import DataProcessor, Params


__all__ = ["angle_to_2pi_range", "check_keypoints", "convert_keypoints_from_albumentations", "convert_keypoints_to_albumentations", "filter_keypoints", "KeypointsProcessor", "KeypointParams"]
keypoint_formats = ...
def angle_to_2pi_range(angle: float) -> float:
    ...

class KeypointParams(Params):
    """
    Parameters of keypoints

    Args:
        format (str): format of keypoints. Should be 'xy', 'yx', 'xya', 'xys', 'xyas', 'xysa'.

            x - X coordinate,

            y - Y coordinate

            s - Keypoint scale

            a - Keypoint orientation in radians or degrees (depending on KeypointParams.angle_in_degrees)
        label_fields (list): list of fields that are joined with keypoints, e.g labels.
            Should be same type as keypoints.
        remove_invisible (bool): to remove invisible points after transform or not
        angle_in_degrees (bool): angle in degrees or radians in 'xya', 'xyas', 'xysa' keypoints
        check_each_transform (bool): if `True`, then keypoints will be checked after each dual transform.
            Default: `True`
    """
    def __init__(self, format: str, label_fields: Optional[Sequence[str]] = ..., remove_invisible: bool = ..., angle_in_degrees: bool = ..., check_each_transform: bool = ...) -> None:
        ...
    
    @classmethod
    def is_serializable(cls) -> bool:
        ...
    
    @classmethod
    def get_class_fullname(cls) -> str:
        ...
    


class KeypointsProcessor(DataProcessor):
    def __init__(self, params: KeypointParams, additional_targets: Optional[Dict[str, str]] = ...) -> None:
        ...
    
    @property
    def default_data_name(self) -> str:
        ...
    
    def ensure_data_valid(self, data: Dict[str, Any]) -> None:
        ...
    
    def ensure_transforms_valid(self, transforms: Sequence[object]) -> None:
        ...
    
    def filter(self, data: Sequence[Sequence], rows: int, cols: int) -> Sequence[Sequence]:
        ...
    
    def check(self, data: Sequence[Sequence], rows: int, cols: int) -> None:
        ...
    
    def convert_from_albumentations(self, data: Sequence[Sequence], rows: int, cols: int) -> List[Tuple]:
        ...
    
    def convert_to_albumentations(self, data: Sequence[Sequence], rows: int, cols: int) -> List[Tuple]:
        ...
    


def check_keypoint(kp: Sequence, rows: int, cols: int) -> None:
    """Check if keypoint coordinates are less than image shapes"""
    ...

def check_keypoints(keypoints: Sequence[Sequence], rows: int, cols: int) -> None:
    """Check if keypoints boundaries are less than image shapes"""
    ...

def filter_keypoints(keypoints: Sequence[Sequence], rows: int, cols: int, remove_invisible: bool) -> Sequence[Sequence]:
    ...

def convert_keypoint_to_albumentations(keypoint: Sequence, source_format: str, rows: int, cols: int, check_validity: bool = ..., angle_in_degrees: bool = ...) -> Tuple:
    ...

def convert_keypoint_from_albumentations(keypoint: Sequence, target_format: str, rows: int, cols: int, check_validity: bool = ..., angle_in_degrees: bool = ...) -> Tuple:
    ...

def convert_keypoints_to_albumentations(keypoints: Sequence[Sequence], source_format: str, rows: int, cols: int, check_validity: bool = ..., angle_in_degrees: bool = ...) -> List[Tuple]:
    ...

def convert_keypoints_from_albumentations(keypoints: Sequence[Sequence], target_format: str, rows: int, cols: int, check_validity: bool = ..., angle_in_degrees: bool = ...) -> List[Tuple]:
    ...

