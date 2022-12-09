from aoctools.datastruct import vec
from operator import eq

with open("input/day9.txt", "r") as f:
    moves = [(l[0], int(l[2:].strip())) for l in f.readlines()]

visited = set((vec(0,0),))
steps = {
    "U": vec(0, -1),
    "D": vec(0, 1),
    "L": vec(-1, 0),
    "R": vec(1, 0),
}

h = vec(0,0)
t = vec(0,0)
def signum(n): return 0 if n == 0 else 1 if n > 0 else -1

for d, n in moves:
    d = steps[d]
    for _ in range(n):
        h += d
        r = h.dist(t) 
        if r <= 1: continue
        
        if r == 2 and any(h.zipm(eq, t)):
            t += (h - t) // 2
        if r > 2:
            t += vec(map(signum, (h-t)))
        visited.add(t)

print(len(visited))

from aoctools.datastruct import vec
from operator import eq

with open("input/day9.txt", "r") as f:
    moves = [(l[0], int(l[2:].strip())) for l in f.readlines()]

visited = set((vec(0,0),))
steps = {
    "U": vec(0, -1),
    "D": vec(0, 1),
    "L": vec(-1, 0),
    "R": vec(1, 0),
}

ts = [vec(0,0) for _ in range(10)]
def signum(n): return 0 if n == 0 else 1 if n > 0 else -1

for d, n in moves:
    d = steps[d]
    for _ in range(n):
        ts[0] += d
        for i in range(1, 10):
            h, t = ts[i-1], ts[i]
            r = h.dist(t) 
            if r <= 1: continue
            
            if r == 2 and any(h.zipm(eq, t)):
                ts[i] += (h - t) // 2
            if r > 2:
                ts[i] += vec(map(signum, (h-t)))
        visited.add(ts[-1])

print(len(visited))