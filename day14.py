with open("input/day14.txt", "r") as f:
    structure = set()
    minx, maxx = 500, 500
    maxy = 0
    for line in f.readlines():
        positions = list(map(lambda p: list(map(int, p.strip().split(","))), line.strip().split('->')))
        for i in range(len(positions) - 1):
            (sx, sy), (ex, ey) = positions[i:i+2]
            xs = (sx, ex)
            ys = (sy, ey)
            for x in range(min(xs), max(xs) + 1):
                for y in range(min(ys), max(ys) + 1):
                    structure.add((x, y))
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    maxy = max(maxy, y)

def f(structure, minx, maxx, maxy):
    counter = 0
    while True:
        s = (500, 0)
        while True:
            x, y = s
            if x < minx or x > maxx or y > maxy:
                return counter
            if not (x, y + 1) in structure:
                s = ((x, y + 1))
            elif not (x - 1, y + 1) in structure:
                s = (x - 1, y + 1)
            elif not (x + 1, y + 1) in structure:
                s = (x + 1, y + 1)
            else:
                structure.add(s)
                counter += 1
                break
print(f(structure, minx, maxx, maxy))

with open("input/day14.txt", "r") as f:
    structure = set()
    minx, maxx = 500, 500
    maxy = 0
    for line in f.readlines():
        positions = list(map(lambda p: list(map(int, p.strip().split(","))), line.strip().split('->')))
        for i in range(len(positions) - 1):
            (sx, sy), (ex, ey) = positions[i:i+2]
            xs = (sx, ex)
            ys = (sy, ey)
            for x in range(min(xs), max(xs) + 1):
                for y in range(min(ys), max(ys) + 1):
                    structure.add((x, y))
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    maxy = max(maxy, y)

m = [[('#' if (x, y) in structure else '.') for x in range(minx - 30, maxx+30)] for y in range(0, maxy + 3)]
def g(structure, maxy):
    counter = 0
    while True:
        s = (500, 0)
        if s in structure:
            return counter
        while True:
            x, y = s
            if y + 1 == maxy + 2:
                structure.add((x, y))
                counter += 1
                break
            elif not (x, y + 1) in structure:
                s = ((x, y + 1))
            elif not (x - 1, y + 1) in structure:
                s = (x - 1, y + 1)
            elif not (x + 1, y + 1) in structure:
                s = (x + 1, y + 1)
            else:
                structure.add(s)
                counter += 1
                break
print(g(structure, maxy))
