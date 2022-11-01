from pathlib import Path
from typing import Literal
from typing_extensions import Self

import numpy as np
import numpy.typing as npt

from .coco_types import Annotation, Category, Image


class COCO:
    def __init__(self, annotation_file: str | Path = ...) -> None:
        """Constructor of Microsoft COCO helper class for reading and visualizing annotations.

        Args:
            annotation_file: Location of annotation file
        """
        ...

    def createIndex(self) -> None:
        ...

    def info(self) -> None:
        """Print information about the annotation file.
        """
        ...

    def getAnnIds(self, imgIds: list[int] = ..., catIds: list[int] = ..., areaRng: list[float] = ..., iscrowd: bool = ...) -> list[int]:
        """Get ann ids that satisfy given filter conditions. default skips that filter.

        Args:
            imgIds: Get anns for given imgs.
            catIds: Get anns for given cats.
            areaRng: Get anns for given area range (e.g. [0 inf]).
            iscrowd: Get anns for given crowd label (False or True).

        Returns:
            Integer array of ann ids.
        """
        ...

    def getCatIds(self, catNms: list[str] = ..., supNms: list[str] = ..., catIds: list[int] = ...) -> list[int]:
        """Get cat ids that satisfy given filter conditions. default skips that filter.

        Args:
            catNms: get cats for given cat names
            supNms get cats for given supercategory names
            catIds: get cats for given cat ids

        Returns:
            ids: integer array of cat ids
        """
        ...

    def getImgIds(self, imgIds: list[int] = ..., catIds: list[int] = ...) -> list[int]:
        """Get img ids that satisfy given filter conditions.

        Args:
            imgIds: get imgs for given ids
            catIds : get imgs with all given cats

        Returns:
            ids: integer array of img ids
        """
        ...

    def loadAnns(self, ids: list[int] = ...) -> list[Annotation]:
        """Load anns with the specified ids.

        Args:
            ids: Integer ids specifying anns.

        Returns:
            anns: loaded ann objects
        """
        ...

    def loadCats(self, ids: list[int] = ...) -> list[Category]:
        """Load cats with the specified ids.

        Args:
            ids: integer ids specifying cats.

        Returns:
            cats: loaded cat objects.
        """
        ...

    def loadImgs(self, ids: list[int] = ...) -> list[Image]:
        """
        Load anns with the specified ids.
            ids: integer ids specifying img

        Returns:
            imgs: loaded img objects
        """
        ...

    def showAnns(self, anns: list[Annotation], draw_bbox: bool = ...) -> None:
        """Display the specified annotations.

        Args:
            anns: Annotations to display.
            draw_bbox: Wether to draw the bounding boxes or not.
        """
        ...

    def loadRes(self, resFile: str) -> Self:
        """Load result file and return a result api object.

        Args:
            resFile: file name of result file

        Returns:
            res: result api object
        """
        ...

    def download(self, tarDir: str = ..., imgIds: list[int] = ...) -> Literal[-1] | None:
        """Download COCO images from mscoco.org server.

        Args:
            tarDir (str): COCO results directory name
            imgIds (list): images to be downloaded
        """
        ...

    def loadNumpyAnnotations(self, data: npt.NDArray[np.float64]) -> list[Annotation]:
        """Convert result data from a numpy array [Nx7] where each row contains {imageID,x1,y1,w,h,score,class}

        Args:
             data (numpy.ndarray)

        Returns:
            annotations (python nested list)
        """
        ...

    def annToRLE(self, ann: Annotation) -> npt.NDArray[np.uint32]:
        """Convert annotation which can be polygons, uncompressed RLE to RLE.

        Returns:
            binary mask (numpy 2D array)
        """
        ...

    def annToMask(self, ann: Annotation) -> npt.NDArray[np.uint32]:
        """Convert annotation which can be polygons, uncompressed RLE, or RLE to binary mask.

        Args:

        Returns:
            binary mask (numpy 2D array)
        """
        ...
