"""
from aoctools.datastruct import vec
ranges = []
ty = 2000000
with open("input/day15.txt", "r") as f:
    for line in f.readlines():
        tokens = line.split()
        sx = int(tokens[2][2:-1])
        sy = int(tokens[3][2:-1])
        bx = int(tokens[8][2:-1])
        by = int(tokens[9][2:])
        
        s = vec(sx, sy)
        b = vec(bx, by)
        d = s.dist(b)
        
        vd = d - abs(sy - ty)
        if vd > 0:
            lx = sx - vd
            rx = sx + vd
            if vec(lx, ty) == b:
                lx += 1
            elif vec(rx, ty) == b:
                rx -= 1
            ranges.append((lx, rx))
ranges.sort(key=lambda r: r[0])

p = -999999999999999
count = 0
for r in ranges:
    if r[1] <= p: continue
    s = max(r[0], p)
    count += (r[1] - s) + 1
    p = r[1] + 1

print(count)
"""
from aoctools.datastruct import vec
from aoctools.datastruct.shapes import box
def Tx(x, y): return x + y
def Ty(x, y): return -x + y

side = 4000000
middle = side // 2
l = Tx(middle, middle - side)
r = Tx(middle + side, middle)
t = Ty(middle, middle - side)
b = Ty(middle - side, middle)

fields = [box(l, r, t, b)]
with open("input/day15.txt", "r") as f:
    for line in f.readlines():
        tokens = line.split()
        sx = int(tokens[2][2:-1])
        sy = int(tokens[3][2:-1])
        bx = int(tokens[8][2:-1])
        by = int(tokens[9][2:])
        
        s = vec(sx, sy)
        b = vec(bx, by)
        d = s.dist(b)
        
        l = Tx(s.x, s.y - d)
        r = Tx(s.x + d, s.y)

        t = Ty(s.x, s.y - d)
        b = Ty(s.x - d, s.y)
        bb = box(l, r, t, b)

        fields = [bc for b in fields for bc in bb.cut(b)]

p = next(filter(lambda b:  b.h.a == b.h.b and b.v.a == b.v.b, fields))
xp = p.h.a
yp = p.v.a

x = (xp - yp) // 2
y = (xp + yp) // 2
print(y + x*4000000)