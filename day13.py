# part 1
class ListOpen: ...
class ListClose: ...
class EOI: ...

def listgen(txt: str):
    buffer = ""
    for c in txt:
        if c == "[":
            yield ListOpen
        elif c == "]":
            if buffer:
                yield int(buffer)
                buffer = ""
            yield ListClose
        elif c == ",":
            if buffer:
                yield int(buffer)
                buffer = ""
        else:
            buffer = buffer + c
    yield EOI

def makelist(g):
    yield ListClose
    for x in g:
        yield x

with open("input/day13.txt", "r") as f:
    indices = 0
    for i, pairs in enumerate(f.read().strip().split("\n\n")):
        i += 1
        l, r = pairs.split("\n")
        lg = listgen(l)
        rg = listgen(r)
        l = next(lg)
        r = next(rg)
        while l != EOI and r != EOI:
            if l == ListOpen and r == ListOpen:
                pass
            elif l == ListClose and r == ListClose:
                pass
            elif r == ListClose:
                break
            elif l == ListClose:
                indices += i
                break
            elif l == ListOpen:
                rg = makelist(rg)
                l = next(lg)
                continue
            elif r == ListOpen:
                lg = makelist(lg)
                r = next(rg)
                continue
            elif l < r:
                indices += i
                break
            elif r < l:
                break

            l = next(lg)
            r = next(rg)
        else: # if one reached EOI
            if l == EOI: indices += i
    print(indices)

# part 2
class ListOpen: ...
class ListClose: ...
class EOI: ...

def listgen(txt: str):
    buffer = ""
    for c in txt:
        if c == "[":
            yield ListOpen
        elif c == "]":
            if buffer:
                yield int(buffer)
                buffer = ""
            yield ListClose
        elif c == ",":
            if buffer:
                yield int(buffer)
                buffer = ""
        else:
            buffer = buffer + c
    yield EOI

def makelist(g):
    yield ListClose
    for x in g:
        yield x

class Packet:
    def __init__(self, s):
        self.s = s
    def __lt__(self, o):
        lg = listgen(self.s)
        rg = listgen(o.s)
        l = next(lg)
        r = next(rg)
        while l != EOI and r != EOI:
            if l == ListOpen and r == ListOpen:
                pass
            elif l == ListClose and r == ListClose:
                pass
            elif r == ListClose:
                break
            elif l == ListClose:
                return True
            elif l == ListOpen:
                rg = makelist(rg)
                l = next(lg)
                continue
            elif r == ListOpen:
                lg = makelist(lg)
                r = next(rg)
                continue
            elif l < r:
                return True
            elif r < l:
                break

            l = next(lg)
            r = next(rg)
        else: # if one reached EOI
            if l == EOI: return True
        return False


with open("input/day13.txt", "r") as f:
    indices = 0
    packets = ["[[6]]", "[[2]]"]
    for pairs in f.read().strip().split("\n\n"):
        l, r = pairs.split("\n")
        packets.append(l)
        packets.append(r)
    
    packets.sort(key=Packet)
    print((packets.index("[[6]]") + 1) * (packets.index("[[2]]") + 1))

