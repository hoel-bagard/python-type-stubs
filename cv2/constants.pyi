# Color conversion codes
COLOR_BGR2GRAY: int
COLOR_BGR2RGB: int
COLOR_GRAY2BGR: int
COLOR_GRAY2RGB: int
COLOR_RGB2BGR: int
COLOR_RGB2GRAY: int

# Fonts
FONT_HERSHEY_COMPLEX: int
FONT_HERSHEY_COMPLEX_SMALL: int
FONT_HERSHEY_DUPLEX: int
FONT_HERSHEY_PLAIN: int
FONT_HERSHEY_SCRIPT_COMPLEX: int
FONT_HERSHEY_SCRIPT_SIMPLEX: int
FONT_HERSHEY_SIMPLEX: int
FONT_HERSHEY_TRIPLEX: int
FONT_ITALIC: int

# ImreadModes
IMREAD_UNCHANGED: int  # If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.
IMREAD_GRAYSCALE: int  # If set, always convert image to the single channel grayscale image (codec internal conversion).
IMREAD_COLOR: int  # If set, always convert image to the 3 channel BGR color image.
IMREAD_ANYDEPTH: int  # If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.
IMREAD_ANYCOLOR: int  # If set, the image is read in any possible color format.
IMREAD_LOAD_GDAL: int  # If set, use the gdal driver for loading the image.
IMREAD_REDUCED_GRAYSCALE_2: int  # If set, always convert image to the single channel grayscale image and the image size reduced 1/2.
IMREAD_REDUCED_COLOR_2: int  # If set, always convert image to the 3 channel BGR color image and the image size reduced 1/2.
IMREAD_REDUCED_GRAYSCALE_4: int  # If set, always convert image to the single channel grayscale image and the image size reduced 1/4.
IMREAD_REDUCED_COLOR_4: int  # If set, always convert image to the 3 channel BGR color image and the image size reduced 1/4.
IMREAD_REDUCED_GRAYSCALE_8: int  # If set, always convert image to the single channel grayscale image and the image size reduced 1/8.
IMREAD_REDUCED_COLOR_8: int  # If set, always convert image to the 3 channel BGR color image and the image size reduced 1/8.
IMREAD_IGNORE_ORIENTATION: int  # If set, do not rotate the image according to EXIF's orientation flag.

# InterpolationFlags
INTER_NEAREST: int  # Nearest neighbor interpolation.
INTER_LINEAR: int  # Bilinear interpolation.
INTER_CUBIC: int  # Bicubic interpolation.
INTER_AREA: int  # Resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_LANCZOS4: int  # Lanczos interpolation over 8x8 neighborhood.
INTER_LINEAR_EXACT: int  # Bit exact bilinear interpolation.
INTER_NEAREST_EXACT: int  # Bit exact nearest neighbor interpolation. This will produce same results as the nearest neighbor method in PIL, scikit-image or Matlab.
INTER_MAX: int  # Mask for interpolation codes.
WARP_FILL_OUTLIERS: int  # Flag, fills all of the destination image pixels. If some of them correspond to outliers in the source image, they are set to zero.
WARP_INVERSE_MAP: int  # Flag, inverse transformation. For example, linearPolar or logPolar transforms: flag is not set: dst(ρ,ϕ)=src(x,y) and flag is set: dst(x,y)=src(ρ,ϕ).

# Line types
FILLED: int
LINE_4: int  # 4-connected line
LINE_8: int  # 8-connected line
LINE_AA: int  # Antialiased line

# WindowFlags
WINDOW_NORMAL: int # The user can resize the window (no constraint) / also use to switch a fullscreen window to a normal size.
WINDOW_AUTOSIZE: int # The user cannot resize the window, the size is constrainted by the image displayed.
WINDOW_OPENGL: int  # Window with opengl support.
WINDOW_FULLSCREEN: int  # Change the window to fullscreen.
WINDOW_FREERATIO: int  # The image expends as much as it can (no ratio constraint).
WINDOW_KEEPRATIO: int  # The ratio of the image is respected.
WINDOW_GUI_EXPANDED: int  # Status bar and tool bar
WINDOW_GUI_NORMAL: int  # Old fashious way

# WindowPropertyFlags
WND_PROP_FULLSCREEN: int  # Fullscreen property (can be WINDOW_NORMAL or WINDOW_FULLSCREEN).
WND_PROP_AUTOSIZE: int  # Autosize property (can be WINDOW_NORMAL or WINDOW_AUTOSIZE).
WND_PROP_ASPECT_RATIO: int  # Window's aspect ration (can be set to WINDOW_FREERATIO or WINDOW_KEEPRATIO).
WND_PROP_OPENGL: int  # Opengl support.
WND_PROP_VISIBLE: int  # Checks whether the window exists and is visible
WND_PROP_TOPMOST: int  # Property to toggle normal window being topmost or not
WND_PROP_VSYNC: int
