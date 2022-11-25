from ..datastruct import vec
import colorsys

class rgb:
    def __init__(self, r, g, b):
        if any(isinstance(i, float) for i in (r, g, b)):
            self._col = vec(float(i) for i in (r, g, b))
        else:
            self._col = vec(i / 255 for i in (r, g, b))
    @staticmethod
    def from_hsv(self, h, s, v):
        return rgb(*colorsys.hsv_to_rgb(h, s, v))
    
    def as_ints(self) -> vec:
        return vec(min(max(int(255*i),0),255) for i in self._col)
    
AOC_GREEN = rgb(0, 153, 5)
AOC_BG    = rgb(15, 15, 35)
AOC_YELLOW = rgb(255, 255, 102)
AOC_WHITE = rgb(204, 204, 204)
AOC_GRAY = rgb(153, 153, 204)
AOC_DARKER = rgb(*(AOC_GRAY._col / 2))

__all__ = [
    "rgb",
    "AOC_GREEN",
    "AOC_GRAY",
    "AOC_BG",
    "AOC_WHITE",
    "AOC_YELLOW",
    "AOC_DARKER"
]