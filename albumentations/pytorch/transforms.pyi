"""
This type stub file was generated by pyright.
"""

from ..core.transforms_interface import BasicTransform

__all__ = ["ToTensorV2"]
def img_to_tensor(im, normalize=...): # -> Tensor:
    ...

def mask_to_tensor(mask, num_classes, sigmoid): # -> Tensor:
    ...

class ToTensor(BasicTransform):
    """Convert image and mask to `torch.Tensor` and divide by 255 if image or mask are `uint8` type.
    This transform is now removed from Albumentations. If you need it downgrade the library to version 0.5.2.

    Args:
        num_classes (int): only for segmentation
        sigmoid (bool, optional): only for segmentation, transform mask to LongTensor or not.
        normalize (dict, optional): dict with keys [mean, std] to pass it into torchvision.normalize

    """
    def __init__(self, num_classes=..., sigmoid=..., normalize=...) -> None:
        ...
    


class ToTensorV2(BasicTransform):
    """Convert image and mask to `torch.Tensor`. The numpy `HWC` image is converted to pytorch `CHW` tensor.
    If the image is in `HW` format (grayscale image), it will be converted to pytorch `HW` tensor.
    This is a simplified and improved version of the old `ToTensor`
    transform (`ToTensor` was deprecated, and now it is not present in Albumentations. You should use `ToTensorV2`
    instead).

    Args:
        transpose_mask (bool): if True and an input mask has three dimensions, this transform will transpose dimensions
        so the shape `[height, width, num_channels]` becomes `[num_channels, height, width]`. The latter format is a
        standard format for PyTorch Tensors. Default: False.
    """
    def __init__(self, transpose_mask=..., always_apply=..., p=...) -> None:
        ...
    
    @property
    def targets(self): # -> dict[str, ((img: ndarray[Unknown, Unknown], **params: Unknown) -> Tensor) | ((mask: Unknown, **params: Unknown) -> Tensor) | ((masks: Unknown, **params: Unknown) -> list[Tensor])]:
        ...
    
    def apply(self, img, **params): # -> Tensor:
        ...
    
    def apply_to_mask(self, mask, **params): # -> Tensor:
        ...
    
    def apply_to_masks(self, masks, **params): # -> list[Tensor]:
        ...
    
    def get_transform_init_args_names(self): # -> tuple[Literal['transpose_mask']]:
        ...
    
    def get_params_dependent_on_targets(self, params): # -> dict[Unknown, Unknown]:
        ...
    

