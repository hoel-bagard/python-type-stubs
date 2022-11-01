import numpy as np
import numpy.typing as npt


def encode(bimask: npt.NDArray[np.uint32]) -> npt.NDArray[np.uint32]:
    ...

def decode(rleObjs: npt.NDArray[np.uint32] | list[int]) -> npt.NDArray[np.uint32]:
    ...

def area(rleObjs: npt.NDArray[np.uint32] | list[int]) -> npt.NDArray[np.uint32]:
    ...

def toBbox(rleObjs: npt.NDArray[np.uint32] | list[int]) -> npt.NDArray[np.uint32]:
    ...
