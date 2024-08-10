from __future__ import annotations
from PIL import Image as PILImage
import cupy.typing as npt
import cupy as np
from dataclasses import dataclass

FloatArray: TypeAlias = npt.NDArray[np.float64]

@dataclass
class ColorArray:
    r: FloatArray
    g: FloatArray
    b: FloatArray
 
    def __add__(self, another: ColorArray) -> ColorArray:
        return ColorArray(self.r + another.r, self.g + another.g, self.b + another.b)

    def __sub__(self, another: ColorArray) -> ColorArray:
        return ColorArray(self.r - another.r, self.g - another.g, self.b - another.b)
    
    def __mul__(self, another: float) -> ColorArray:
        return ColorArray(self.r * another, self.g * another, self.b * another)
    
    def __truediv__(self, another: float) -> ColorArray:
        return ColorArray(self.r / another, self.g / another, self.b / another)

@dataclass
class Color:
    r: float
    g: float
    b: float
 
    def __add__(self, another: Color) -> Color:
        return Color(self.r + another.r, self.g + another.g, self.b + another.b)

    def __sub__(self, another: Color) -> Color:
        return Color(self.r - another.r, self.g - another.g, self.b - another.b)
    
    def __mul__(self, another: float) -> Color:
        return Color(self.r * another, self.g * another, self.b * another)
    
    def __truediv__(self, another: float) -> Color:
        return Color(self.r / another, self.g / another, self.b / another)

class Image:
    _img: PILImage.Image

    def __init__(self, width: int, height: int) -> None:
        self._img = PILImage.new('RGB', (width, height))
    
    """
    Color values must be in [0.0, 1.0] interval.
    """
    def set_pixel(self, x: int, y: int, color: Color) -> None:
        r = int(color.r * 255)
        g = int(color.g * 255)
        b = int(color.b * 255)

        self._img.putpixel((x, y), (r, g, b))

    def save(self, filepath: str) -> None:
        self._img.save(filepath)