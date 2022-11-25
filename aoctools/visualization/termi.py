from typing import Union
from colorsys import hsv_to_rgb
from time import monotonic
from types import NoneType
import re

from .ansi import Color, BOLD, RESET, NORMAL, CursorUp, CursorDown, CursorLeft, CursorRight, CursorPosition
from ..datastruct import vec
from ..functional import maybe, mapm, ifelse
from ..util import partition, map_partition, patternize

def _parse_color(c, lv):
    if c is None or isinstance(c, Color):
        return c
    elif isinstance(c, tuple):
        return Color(*c, level=lv)
    else:
        return Color(c, level=lv)

def _adapt_text(text):
    return text                 \
        .replace("\t", "    ")  \
        .replace("\r\n", "\n")  \
        .replace("\r", "")

class Text:
    def __init__(self, *elms: Union[str, "Text"], color: Color =None, bg: Color = None, bold: bool = None):
        self._elements = list(map(lambda e: e if isinstance(e, Text) else _adapt_text(e), elms))
        self.set_color(color, update=False)
        self.set_bgcolor(bg, update=False)
        self.set_bold(bold, update=False)
        self._has_color = self._col is not None or self._bcol is not None
        self.update()

    def set_color(self, color: Color, update=True):
        self._col = _parse_color(color, "fg")
        if update:
            self.update()

    def set_bgcolor(self, color: Color, update=True):
        self._bcol = _parse_color(color, "bg")
        if update:
            self.update()

    def set_bold(self, bold: Union[NoneType, bool], update=True):
        self._bold = mapm(lambda b: ifelse(b, BOLD, NORMAL), bold)
        self._bold_arg = bold
        if update:
            self.update()

    def update_color(self, color: Color):
        if self._col is None:
            self.set_color(color, update=False)
    def update_bgcolor(self, color: Color):
        if self._bcol is None:
            self.set_bgcolor(color, update=False)
    def update_bold(self, bold: bool):
        if self._bold_arg is None:
            self.set_bold(bold, update=False)

    def update(self):
        for elem in self._elements:
            if isinstance(elem, Text):
                elem.update_color(self._col)
                elem.update_bgcolor(self._bcol)
                elem.update_bold(self._bold_arg)
                elem.update()

    def attribs(self):
        return maybe("", str, self._col) + \
            maybe("", str, self._bcol) + \
            maybe("", str, self._bold)

    def __repr__(self):
        els = list(map(repr, self._elements))
        col = [repr(self._col)] if self._col is not None else []
        bgcol = [repr(self._bcol)] if self._bcol is not None else []
        bld = [repr(self._bold)] if self._bold is not None else []
        return "Text(" + ", ".join(els + col + bgcol + bld) + ")"

    def _render_sub(self, index, element, attr):
        last_element = index == len(self._elements) - 1
        if last_element:
            cleanup_directive = "none"
        elif self._has_color:
            cleanup_directive = "attributes"
        else:
            cleanup_directive = "full"

        if isinstance(element, str):
            return element
        else:
            return element.render(cleanup=cleanup_directive) + \
                ("" if last_element else attr)

    def render(self, cleanup="full", scope: dict = None):
        attr = self.attribs()
        if cleanup == "full":
            end = str(RESET)
        elif cleanup == "attributes" and self._bold:
            end = str(NORMAL)
        else:
            end = ""

        return attr + \
            "".join(map(lambda i: self._render_sub(*i, attr), enumerate(self._elements))) + \
            end
    def __str__(self): return self.render()

    def movement(self):
        cursor = vec(0,0)
        for element in self._elements:
            if isinstance(element, Text):
                cursor += element.movement()
            else:
                for c in element:
                    if c == '\r':
                        cursor = vec(0, cursor.y)
                    elif c == '\n':
                        cursor = vec(0, cursor.y + 1)
                    else:
                        cursor += vec(1, 0)
        return cursor

    def width(self):
        cursor = vec(0,0)
        maxw = 0
        for element in self._elements:
            if isinstance(element, Text):
                cursor += element.movement()
            else:
                for c in element:
                    if c == '\r':
                        cursor = vec(0, cursor.y)
                    elif c == '\n':
                        cursor = vec(0, cursor.y + 1)
                    else:
                        cursor += vec(1, 0)
            maxw = max(cursor.x, maxw)
        return maxw
    def partition1(self, pattern: str):
        pair = None
        for i, e in enumerate(self._elements):
            if isinstance(e, str):
                j = e.find(pattern)
                if j != -1: 
                    pair = e[:j], e[j:j+len(pattern)], e[j+len(pattern):]
                    break
            else:
                res = e.partition1(pattern)
                if res is not None: 
                    pair = res
                    break

        if pair is None:
            return None
        left, center, right = pair
        return Text(*self._elements[:i], left, color=self._col, bg=self._bcol, bold=self._bold_arg), \
            Text(center, color=self._col, bg=self._bcol, bold=self._bold_arg), \
            Text(right, *self._elements[i+1:], color=self._col, bg=self._bcol, bold=self._bold_arg)

    def partition(self, pattern: str, times=-1):
        counter = 0
        elem = self
        while times < 0 or counter < times:
            splt = elem.partition1(pattern)
            if not splt:
               break

            left, center, right = splt
            yield left
            yield center

            elem = right
            counter += 1
        yield elem

    def split(self, pattern: str, times=-1):
        for i, elem in enumerate(self.partition(pattern, times)):
            if i % 2 == 0:
                yield elem

    def reset_movement(self):
        return vec_to_reset(self.movement())

    def equivalent(self, text: str):
        return Text(text, color=self._col, bg=self._bcol, bold=self._bold_arg)
    
    def highlight(self, pattern: str, template: "Text"):
        p = patternize(pattern)
        elems = []
        for e in self._elements:
            if isinstance(e, str):
                elems.extend(
                    map_partition(template.equivalent,partition(e, p))
                )
            else:
                elems.append(e)
        return Text(*elems, color=self._col, bg=self._bcol, bold=self._bold_arg)
    
    def append(self, t):
        self._elements.append(t)
    def prepend(self, t):
        self._elements = [t] + self._elements


def vec_to_reset(pos: vec):
    left, up = pos
    cleft = str(CursorLeft(str(left))) if left > 0 else ""
    cup = str(CursorUp(str(up))) if up > 0 else ""
    return cleft + cup

def vec_to_movement(pos: vec):
    right, down = pos
    cright = str(CursorRight(str(right))) if right > 0 else ""
    cdown = str(CursorDown(str(down))) if down > 0 else ""
    return cright + cdown

def rainbow(text):
    return Text(*(Text(c, color=hsv_to_rgb((i%10)/10, 1, 1)) for i, c in enumerate(text)))

def statusbar(prompt, i, j, /, 
    bar=40, 
    prompt_size=0, 
    dynamic=False,
    fg = "blue",
    bg = "gray"
    ):
    status = bar * min(i, j) // j
    status_txt = Text(status * ' ', bg=fg)
    remainder = Text((bar-status) * ' ', bg=bg)
    if dynamic:
        loading = "◒◐◓◑"[int((monotonic() % 0.5) / 0.5 * 4)] if i < j else Text('●', color="green")
    else:
        loading = ""
    jstr = str(j)
    istr = str(min(i, j)).rjust(len(jstr))
    return Text((prompt + ":").ljust(prompt_size) + " ", istr,"/", jstr, " ", status_txt, remainder, " ", loading)



def print_reset(text):
    if not isinstance(text, Text | TextBox):
        text = Text(text)
    print(str(text) + text.reset_movement(), end="", flush=True)

def print_all(*obj):
    print("".join(str(o) + o.reset_movement() for o in obj), end="", flush=True)

class TextBox:
    def __init__(self, text: Union[Text, str], pos: vec):
        t = text if isinstance(text, Text) else Text(text)
        self._text = text
        self._rows = list(self._text.split("\n"))
        self._pos = pos

    def render(self):
        rowstrings = [str(CursorDown(str(self._pos.y)))] if self._pos.y > 0 else []
        for row in self._rows:
            buffer = str(CursorRight(str(self._pos.x))) if self._pos.x > 0 else ""
            buffer += row.render() + "\n"
            rowstrings.append(buffer)

        return "".join(rowstrings)

    def movement(self):
        w = self._rows[-1].movement().x
        lns = len(self._rows)
        return self._pos + vec(w, lns)

    def reset_movement(self):
        return vec_to_reset(self.movement())

    def bottom_right(self):
        return vec_to_movement(self.movement())

    def width(self):
        return max(r.movement().x for r in self._rows)

    def pad(self, n=0):
        widths = list(map(lambda r: r.movement().x, self._rows))
        mw = max(widths) + n
        for r, w in zip(self._rows, widths):
            if w < mw:
                r.append((mw - w) * " ")

    def indent(self, n):
        txt = " " * n
        for r in self._rows:
            r.prepend(txt)

    def __repr__(self) -> str:
        return f"Text({repr(self._text)}, {repr(self._pos)})"

    def __str__(self) -> str: 
        return self.render()

def highlight(text, pattern: Union[str, re.Pattern], template: Text):
    return Text(text).highlight(pattern, template)



__all__ = ["Text",
    "rainbow",
    "statusbar",
    "print_reset",
    "print_all",
    "TextBox",
    "vec_to_movement",
    "vec_to_reset",
    "highlight",
]