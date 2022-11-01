from typing import Literal, Optional

import numpy as np
import numpy.typing as npt

from .coco import COCO
from .coco_types import EvaluationResult

T_IOU = Literal["segm", "bbox", "keypoints"]


class COCOeval:
    def __init__(self, cocoGt: COCO = ..., cocoDt: COCO = ..., iouType: T_IOU = ...) -> None:
        """Initialize CocoEval using coco APIs for gt and dt

        Args:
            cocoGt: coco object with ground truth annotations
            cocoDt: coco object with detection results
        """
        ...

    def evaluate(self) -> None:
        """Run per image evaluation on given images and store results (a list of dict) in self.evalImgs"""
        ...

    def computeIoU(self, imgId: int, catId: int) -> list[float]:
        ...

    def computeOks(self, imgId: int, catId: int) -> npt.NDArray[np.float64]:
        ...

    def evaluateImg(self, imgId: int, catId: int, aRng: list[int], maxDet: int) -> EvaluationResult:
        """Perform evaluation for single category and image.

        Returns:
            dict (single image results)
        """
        ...

    def accumulate(self, p: Optional[Params] = ...) -> None:
        """Accumulate per image evaluation results and store the result in self.eval

        Args:
            p: input params for evaluation
        """
        ...

    def summarize(self) -> None:
        """Compute and display summary metrics for evaluation results.

        Note this functin can *only* be applied on the default parameter setting
        """
        ...

    def __str__(self) -> str:
        ...



class Params:
    """Params for coco evaluation api"""
    def setDetParams(self) -> None:
        ...

    def setKpParams(self) -> None:
        ...

    def __init__(self, iouType: T_IOU = ...) -> None:
        ...



