from ..datastruct import vec
from .color import rgb
class CSI:
    def __init__(self, *args):
        self._csi = "\x1b["
        self._arg = args

    def __init_subclass__(cls, /, terminator) -> None:
        cls._term = terminator

    def __str__(self):
        return self._csi + ";".join(self._arg) + self._term
    
    def __repr__(self):
        return "ESC[" + ";".join(self._arg) + self._term




class CursorPosition(CSI, terminator="H"):
    def __init__(self, pos: vec):
        assert len(pos) == 2
        super().__init__(*map(str, reversed(pos)))

class CursorUp(CSI, terminator="A"): ...
class CursorDown(CSI, terminator="B"): ...
class CursorRight(CSI, terminator="C"): ...
class CursorLeft(CSI, terminator="D"): ...

COLORS = {
    'fg': {
        'black': '30', 
        'red': '31', 
        'green': '32', 
        'yellow': '33', 
        'blue': '34', 
        'magenta': '35', 
        'cyan': '36', 
        'white': '37', 
        'gray': '90', 
        'bright red': '91', 
        'bright green': '92', 
        'bright yellow': '93', 
        'bright blue': '94', 
        'bright magenta': '95', 
        'bright cyan': '96', 
        'bright white': '97',
        '_color_256': ['38', '5'],
        '_color_rgb': ['38', '2'],
    },
    'bg': {
        'black': '40', 
        'red': '41', 
        'green': '42', 
        'yellow': '43', 
        'blue': '44', 
        'magenta': '45', 
        'cyan': '46', 
        'white': '47', 
        'gray': '100', 
        'bright red': '101', 
        'bright green': '102', 
        'bright yellow': '103', 
        'bright blue': '104', 
        'bright magenta': '105', 
        'bright cyan': '106', 
        'bright white': '107',
        '_color_256': ['48', '5'],
        '_color_rgb': ['48', '2'],
    }
}



class Attributes(CSI, terminator="m"):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__("m")

RESET = Attributes("")
BOLD = Attributes("1")
FAINT = Attributes("2")
NORMAL = Attributes("22")


class Color(Attributes):
    def __init__(self, *args, level="fg"):
        if len(args) == 1:
            if isinstance(args[0], str):
                super().__init__(COLORS[level][args[0].lower()])
            elif isinstance(args[0], rgb):
                super().__init__(*COLORS[level]["_color_rgb"], *map(str, args[0].as_ints()))
            else:
                super().__init__(*COLORS[level]["_color_256"], str(args[0]))
        else:
            if any((isinstance(i, float) for i in args)):
                args = map(lambda i: int(max(min(255*i, 255), 0)), args)
            super().__init__(*COLORS[level]["_color_rgb"], *map(str, args))


__all__ = [
    "RESET",
    "BOLD",
    "FAINT",
    "NORMAL",
    "Attributes",
    "Color",
    "CSI",
]