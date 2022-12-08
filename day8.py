# part 1
from itertools import accumulate
with open("input/day8.txt") as f:
    data = [list(map(int, l.strip())) for l in f.readlines()]

h, w = len(data), len(data[0])
data_t = [[data[x][y] for x in range(h)] for y in range(w)]

from_l = [list(accumulate(r, func=max)) for r in data]
from_r = [list(reversed(list(accumulate(reversed(r), func=max)))) for r in data]

from_u_t = [list(accumulate(r, func=max)) for r in data_t]
from_d_t = [list(reversed(list(accumulate(reversed(r), func=max)))) for r in data_t]


def idata(g, w, h, x, y):
    if x >= w or x < 0: return -1    
    if y >= h or y < 0: return -1
    return g[y][x]

a = 0
for y, r in enumerate(data):
    for x, c in enumerate(r):
        if (c > idata(from_l, w, h, x-1, y) or c > idata(from_r, w, h, x+1, y) or c > idata(from_u_t, h, w, y-1, x) or c > idata(from_d_t, h, w, y+1, x)):
            a += 1

print(a)

# part 2
from itertools import takewhile
with open("input/day8.txt") as f:
    data = [list(map(int, l.strip())) for l in f.readlines()]

h, w = len(data), len(data[0])
data_t = [[data[x][y] for x in range(h)] for y in range(w)]

s = 0
for y, r in enumerate(data[1:-1]):
    y += 1
    for x, c in enumerate(r[1:-1]):
        x += 1
        r = len(list(takewhile(lambda t: t < c, data[y][x+1:]))) + 1
        l = len(list(takewhile(lambda t: t < c, reversed(data[y][:x])))) + 1
        d = len(list(takewhile(lambda t: t < c, data_t[x][y+1:]))) + 1
        u = len(list(takewhile(lambda t: t < c, reversed(data_t[x][:y])))) + 1

        r = min(r, w - x - 1)
        l = min(l, x)
        d = min(d, h - y - 1)
        u = min(u, y)

        s = max(s, r*l*u*d)

print(s)

# part 1 (how it should have been, faster and simpler to implement)
with open("input/day8.txt") as f:
    data = [list(map(int, l.strip())) for l in f.readlines()]

h, w = len(data), len(data[0])
data_t = [[data[x][y] for x in range(h)] for y in range(w)]

aa = 0
for y, r in enumerate(data):
    for x, c in enumerate(r):
        if (all(map(lambda t: t < c, data[y][x+1:])) or \
            all(map(lambda t: t < c, data[y][:x])) or \
            all(map(lambda t: t < c, data_t[x][y+1:])) or \
            all(map(lambda t: t < c, data_t[x][:y]))):
            aa += 1
assert a == aa