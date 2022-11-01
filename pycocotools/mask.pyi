import numpy as np
import numpy.typing as npt

from .coco_types import EncodedRLE

def encode(bimask: npt.NDArray[np.uint8]) -> EncodedRLE:
    ...

def decode(rleObjs: EncodedRLE) -> npt.NDArray[np.uint8]:
    ...

def area(rleObjs: EncodedRLE) -> np.uint32:
    ...

def toBbox(rleObjs: EncodedRLE) -> npt.NDArray[np.float64]:
    ...
