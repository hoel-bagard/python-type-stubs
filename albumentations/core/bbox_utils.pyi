"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List, Optional, Sequence, TypeVar

from .transforms_interface import BoxInternalType, BoxType
from .utils import DataProcessor, Params


__all__ = ["normalize_bbox", "denormalize_bbox", "normalize_bboxes", "denormalize_bboxes", "calculate_bbox_area", "filter_bboxes_by_visibility", "convert_bbox_to_albumentations", "convert_bbox_from_albumentations", "convert_bboxes_to_albumentations", "convert_bboxes_from_albumentations", "check_bbox", "check_bboxes", "filter_bboxes", "union_of_bboxes", "BboxProcessor", "BboxParams"]
TBox = TypeVar("TBox", BoxType, BoxInternalType)
class BboxParams(Params):
    """
    Parameters of bounding boxes

    Args:
        format (str): format of bounding boxes. Should be 'coco', 'pascal_voc', 'albumentations' or 'yolo'.

            The `coco` format
                `[x_min, y_min, width, height]`, e.g. [97, 12, 150, 200].
            The `pascal_voc` format
                `[x_min, y_min, x_max, y_max]`, e.g. [97, 12, 247, 212].
            The `albumentations` format
                is like `pascal_voc`, but normalized,
                in other words: `[x_min, y_min, x_max, y_max]`, e.g. [0.2, 0.3, 0.4, 0.5].
            The `yolo` format
                `[x, y, width, height]`, e.g. [0.1, 0.2, 0.3, 0.4];
                `x`, `y` - normalized bbox center; `width`, `height` - normalized bbox width and height.
        label_fields (list): list of fields that are joined with boxes, e.g labels.
            Should be same type as boxes.
        min_area (float): minimum area of a bounding box. All bounding boxes whose
            visible area in pixels is less than this value will be removed. Default: 0.0.
        min_visibility (float): minimum fraction of area for a bounding box
            to remain this box in list. Default: 0.0.
        check_each_transform (bool): if `True`, then bboxes will be checked after each dual transform.
            Default: `True`
    """
    def __init__(self, format: str, label_fields: Optional[Sequence[str]] = ..., min_area: float = ..., min_visibility: float = ..., check_each_transform: bool = ...) -> None:
        ...
    
    @classmethod
    def is_serializable(cls) -> bool:
        ...
    
    @classmethod
    def get_class_fullname(cls) -> str:
        ...
    


class BboxProcessor(DataProcessor):
    def __init__(self, params: BboxParams, additional_targets: Optional[Dict[str, str]] = ...) -> None:
        ...
    
    @property
    def default_data_name(self) -> str:
        ...
    
    def ensure_data_valid(self, data: Dict[str, Any]) -> None:
        ...
    
    def filter(self, data: Sequence, rows: int, cols: int) -> List:
        ...
    
    def check(self, data: Sequence, rows: int, cols: int) -> None:
        ...
    
    def convert_from_albumentations(self, data: Sequence, rows: int, cols: int) -> List[BoxType]:
        ...
    
    def convert_to_albumentations(self, data: Sequence[BoxType], rows: int, cols: int) -> List[BoxType]:
        ...
    


def normalize_bbox(bbox: TBox, rows: int, cols: int) -> TBox:
    """Normalize coordinates of a bounding box. Divide x-coordinates by image width and y-coordinates
    by image height.

    Args:
        bbox: Denormalized bounding box `(x_min, y_min, x_max, y_max)`.
        rows: Image height.
        cols: Image width.

    Returns:
        Normalized bounding box `(x_min, y_min, x_max, y_max)`.

    Raises:
        ValueError: If rows or cols is less or equal zero

    """
    ...

def denormalize_bbox(bbox: TBox, rows: int, cols: int) -> TBox:
    """Denormalize coordinates of a bounding box. Multiply x-coordinates by image width and y-coordinates
    by image height. This is an inverse operation for :func:`~albumentations.augmentations.bbox.normalize_bbox`.

    Args:
        bbox: Normalized bounding box `(x_min, y_min, x_max, y_max)`.
        rows: Image height.
        cols: Image width.

    Returns:
        Denormalized bounding box `(x_min, y_min, x_max, y_max)`.

    Raises:
        ValueError: If rows or cols is less or equal zero

    """
    ...

def normalize_bboxes(bboxes: Sequence[BoxType], rows: int, cols: int) -> List[BoxType]:
    """Normalize a list of bounding boxes.

    Args:
        bboxes: Denormalized bounding boxes `[(x_min, y_min, x_max, y_max)]`.
        rows: Image height.
        cols: Image width.

    Returns:
        Normalized bounding boxes `[(x_min, y_min, x_max, y_max)]`.

    """
    ...

def denormalize_bboxes(bboxes: Sequence[BoxType], rows: int, cols: int) -> List[BoxType]:
    """Denormalize a list of bounding boxes.

    Args:
        bboxes: Normalized bounding boxes `[(x_min, y_min, x_max, y_max)]`.
        rows: Image height.
        cols: Image width.

    Returns:
        List: Denormalized bounding boxes `[(x_min, y_min, x_max, y_max)]`.

    """
    ...

def calculate_bbox_area(bbox: BoxType, rows: int, cols: int) -> int:
    """Calculate the area of a bounding box in pixels.

    Args:
        bbox: A bounding box `(x_min, y_min, x_max, y_max)`.
        rows: Image height.
        cols: Image width.

    Return:
        Area of a bounding box in pixels.

    """
    ...

def filter_bboxes_by_visibility(original_shape: Sequence[int], bboxes: Sequence[BoxType], transformed_shape: Sequence[int], transformed_bboxes: Sequence[BoxType], threshold: float = ..., min_area: float = ...) -> List[BoxType]:
    """Filter bounding boxes and return only those boxes whose visibility after transformation is above
    the threshold and minimal area of bounding box in pixels is more then min_area.

    Args:
        original_shape: Original image shape `(height, width, ...)`.
        bboxes: Original bounding boxes `[(x_min, y_min, x_max, y_max)]`.
        transformed_shape: Transformed image shape `(height, width)`.
        transformed_bboxes: Transformed bounding boxes `[(x_min, y_min, x_max, y_max)]`.
        threshold: visibility threshold. Should be a value in the range [0.0, 1.0].
        min_area: Minimal area threshold.

    Returns:
        Filtered bounding boxes `[(x_min, y_min, x_max, y_max)]`.

    """
    ...

def convert_bbox_to_albumentations(bbox: BoxType, source_format: str, rows: int, cols: int, check_validity: bool = ...) -> BoxType:
    """Convert a bounding box from a format specified in `source_format` to the format used by albumentations:
    normalized coordinates of top-left and bottom-right corners of the bounding box in a form of
    `(x_min, y_min, x_max, y_max)` e.g. `(0.15, 0.27, 0.67, 0.5)`.

    Args:
        bbox: A bounding box tuple.
        source_format: format of the bounding box. Should be 'coco', 'pascal_voc', or 'yolo'.
        check_validity: Check if all boxes are valid boxes.
        rows: Image height.
        cols: Image width.

    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.

    Note:
        The `coco` format of a bounding box looks like `(x_min, y_min, width, height)`, e.g. (97, 12, 150, 200).
        The `pascal_voc` format of a bounding box looks like `(x_min, y_min, x_max, y_max)`, e.g. (97, 12, 247, 212).
        The `yolo` format of a bounding box looks like `(x, y, width, height)`, e.g. (0.3, 0.1, 0.05, 0.07);
        where `x`, `y` coordinates of the center of the box, all values normalized to 1 by image height and width.

    Raises:
        ValueError: if `target_format` is not equal to `coco` or `pascal_voc`, ot `yolo`.
        ValueError: If in YOLO format all labels not in range (0, 1).

    """
    ...

def convert_bbox_from_albumentations(bbox: BoxType, target_format: str, rows: int, cols: int, check_validity: bool = ...) -> BoxType:
    """Convert a bounding box from the format used by albumentations to a format, specified in `target_format`.

    Args:
        bbox: An albumentations bounding box `(x_min, y_min, x_max, y_max)`.
        target_format: required format of the output bounding box. Should be 'coco', 'pascal_voc' or 'yolo'.
        rows: Image height.
        cols: Image width.
        check_validity: Check if all boxes are valid boxes.

    Returns:
        tuple: A bounding box.

    Note:
        The `coco` format of a bounding box looks like `[x_min, y_min, width, height]`, e.g. [97, 12, 150, 200].
        The `pascal_voc` format of a bounding box looks like `[x_min, y_min, x_max, y_max]`, e.g. [97, 12, 247, 212].
        The `yolo` format of a bounding box looks like `[x, y, width, height]`, e.g. [0.3, 0.1, 0.05, 0.07].

    Raises:
        ValueError: if `target_format` is not equal to `coco`, `pascal_voc` or `yolo`.

    """
    ...

def convert_bboxes_to_albumentations(bboxes: Sequence[BoxType], source_format, rows, cols, check_validity=...) -> List[BoxType]:
    """Convert a list bounding boxes from a format specified in `source_format` to the format used by albumentations"""
    ...

def convert_bboxes_from_albumentations(bboxes: Sequence[BoxType], target_format: str, rows: int, cols: int, check_validity: bool = ...) -> List[BoxType]:
    """Convert a list of bounding boxes from the format used by albumentations to a format, specified
    in `target_format`.

    Args:
        bboxes: List of albumentation bounding box `(x_min, y_min, x_max, y_max)`.
        target_format: required format of the output bounding box. Should be 'coco', 'pascal_voc' or 'yolo'.
        rows: Image height.
        cols: Image width.
        check_validity: Check if all boxes are valid boxes.

    Returns:
        List of bounding boxes.

    """
    ...

def check_bbox(bbox: BoxType) -> None:
    """Check if bbox boundaries are in range 0, 1 and minimums are lesser then maximums"""
    ...

def check_bboxes(bboxes: Sequence[BoxType]) -> None:
    """Check if bboxes boundaries are in range 0, 1 and minimums are lesser then maximums"""
    ...

def filter_bboxes(bboxes: Sequence[BoxType], rows: int, cols: int, min_area: float = ..., min_visibility: float = ...) -> List[BoxType]:
    """Remove bounding boxes that either lie outside of the visible area by more then min_visibility
    or whose area in pixels is under the threshold set by `min_area`. Also it crops boxes to final image size.

    Args:
        bboxes: List of albumentation bounding box `(x_min, y_min, x_max, y_max)`.
        rows: Image height.
        cols: Image width.
        min_area: Minimum area of a bounding box. All bounding boxes whose visible area in pixels.
            is less than this value will be removed. Default: 0.0.
        min_visibility: Minimum fraction of area for a bounding box to remain this box in list. Default: 0.0.

    Returns:
        List of bounding boxes.

    """
    ...

def union_of_bboxes(height: int, width: int, bboxes: Sequence[BoxType], erosion_rate: float = ...) -> BoxType:
    """Calculate union of bounding boxes.

    Args:
        height (float): Height of image or space.
        width (float): Width of image or space.
        bboxes (List[tuple]): List like bounding boxes. Format is `[(x_min, y_min, x_max, y_max)]`.
        erosion_rate (float): How much each bounding box can be shrinked, useful for erosive cropping.
            Set this in range [0, 1]. 0 will not be erosive at all, 1.0 can make any bbox to lose its volume.

    Returns:
        tuple: A bounding box `(x_min, y_min, x_max, y_max)`.

    """
    ...

