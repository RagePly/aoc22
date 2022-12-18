# part 1
with open("input/day18.txt", "r") as f:
    lava = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
count = 0
for (i, ci) in enumerate(lava):
    sides = [True for _ in range(6)]
    p1 = (ci[0] + 1, ci[1], ci[2])
    p2 = (ci[0] - 1, ci[1], ci[2])
    p3 = (ci[0], ci[1] + 1, ci[2])
    p4 = (ci[0], ci[1] - 1, ci[2])
    p5 = (ci[0], ci[1], ci[2] + 1)
    p6 = (ci[0], ci[1], ci[2] - 1)
    for (j, cj) in enumerate(lava):
        if i == j: continue
        if (p1 == cj):
            sides[0] = False
        elif (p2 == cj):
            sides[1] = False
        elif (p3 == cj):
            sides[2] = False
        elif (p4 == cj):
            sides[3] = False
        elif (p5 == cj):
            sides[4] = False
        elif (p6 == cj):
            sides[5] = False

    count += sum((1 if s else 0) for s in sides)

print(count)
# part 2
with open("input/day18.txt", "r") as f:
    lava = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
h = max(map(lambda x: x[0], lava)) + 1
w = max(map(lambda x: x[1], lava)) + 1
d = max(map(lambda x: x[2], lava)) + 1
volume = [[[[False, False, False] for _ in range(d)] for _ in range(w)] for _ in range(h)]

for ci in lava:
    volume[ci[0]][ci[1]][ci[2]][0] = True


def fill(x, y, z):
    global volume, h, w, d
    p = [(x, y, z)]
    visited = []
    flag = False
    while p:
        x, y, z = p.pop()
        if volume[x][y][z][1]: continue
        
        volume[x][y][z][1] = True
        visited.append((x, y, z))

        dirs = [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]

        for xp, yp, zp in dirs:
            if xp >= h or xp < 0 or yp >= w or yp < 0 or zp >= d or zp < 0:
                flag = True
            elif not volume[xp][yp][zp][0]:
                p.append((xp, yp, zp))

    if flag:
        for (x,y,z) in visited:
            volume[x][y][z][2] = True

for i in range(h):
    for j in range(w):
        for k in range(d):
            if (not volume[i][j][k][0]) and (not volume[i][j][k][1]):
                fill(i, j, k)

count = 0
for i in range(h):
    for j in range(w):
        for k in range(d):
            if volume[i][j][k][0]:
                dirs = [
                    (i + 1, j, k),
                    (i - 1, j, k),
                    (i, j + 1, k),
                    (i, j - 1, k),
                    (i, j, k + 1),
                    (i, j, k - 1),
                ]
                for (x, y, z) in dirs:
                    if x >= h or x < 0 or y >= w or y < 0 or z >= d or z < 0:
                        count += 1
                    elif (not volume[x][y][z][0]) and volume[x][y][z][2]:
                        count += 1

print(count)