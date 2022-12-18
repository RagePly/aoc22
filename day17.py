pieces = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
pieces = [[[c == "#" for c in line] for line in piece.split("\n")] for piece in pieces.split("\n\n")]
pieces = [(piece, len(piece), len(piece[0]))  for piece in pieces]
with open("input/day17.txt", "r") as f:
    mov = [c == ">" for c in f.read().strip()]

def piece_iter(p,x,y):
    for i, r in enumerate(p):
        for j, c in enumerate(r):
            if c:
                yield x + j, y - i

tower = [(0, 0, [[True for _ in range(7)]])]

def is_hit(piece, tower, x, y, h):
    piece = piece
    for (yp, xp, place) in tower:
        if yp < y - h: break
        for px, py in piece_iter(piece, x, y):
            for tx, ty in piece_iter(place, xp, yp):
                if py == ty and px == tx:
                    return True
    return False

j = 0
for i in range(2022):
    piece, h, w = pieces[i%len(pieces)]
    y, x = tower[0][0] + 3 + h, 2
    while True:
        if mov[j%len(mov)]:
            if x + w < 7 and not is_hit(piece, tower, x + 1, y, h):
                x += 1
        else:
            if x - 1 >= 0 and not is_hit(piece, tower, x - 1, y, h):
                x -= 1
        j += 1
        hit = False
        if is_hit(piece, tower, x, y - 1, h):
            tower.append((y, x, piece))
            tower.sort(key=lambda x: x[0], reverse=True)
            break
        y -= 1
print(tower[0][0])

# part 2
pieces = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""

pieces = [[[c == "#" for c in line] for line in piece.split("\n")] for piece in pieces.split("\n\n")]
pieces = [(piece, len(piece), len(piece[0]))  for piece in pieces]
with open("input/day17.txt", "r") as f:
    mov = [c == ">" for c in f.read().strip()]

def piece_iter(p,x,y):
    for i, r in enumerate(p):
        for j, c in enumerate(r):
            if c:
                yield x + j, y - i

def peice_hit(p1, p2):
    p1, x1, y1 = p1
    p2, x2, y2 = p2
    for x, y in piece_iter(p1, x1, y1):
        for xp, yp in piece_iter(p2, x2, y2):
            if x == xp and y == yp: return True
    return False


isect = {(i, j): set() for i in range(len(pieces)) for j in range(len(pieces))}
for i, (p, h, w) in enumerate(pieces):
    for j, (pp, hp, wp) in enumerate(pieces):
        x, y = wp - 1, h + hp - 2
        for xp in range(0, (w + wp - 2) + 1):
            for yp in range(hp - 1, (h + 2*hp - 3) + 1):
                if peice_hit((p, x, y), (pp, xp, yp)):
                    isect[(i, j)].add((xp - x, yp - y))

def intersect(i, xi, yi, j, xj, yj):
    global isect
    return (xj - xi, yj - yi) in isect[(i, j)]

def hits_tower(tower, i, x, y, h):
    for (yp, xp, j) in tower:
        if yp < y - h: break
        if intersect(i, x, y, j, xp, yp):
            return True
    return False

tower = []
order = []
k = 0
oi, oip = 0, 0
flag = False
for r in range(10000):
    i = r%len(pieces)
    piece, h, w = pieces[i]
    y, x, j = (tower[0][0] + 3 + h, 2, tower[-1]) if len(tower)>0 else (3 + h, 2, None)
    while True:
        if mov[k%len(mov)]:
            if x + w < 7 and (j is None or not hits_tower(tower, i, x+1, y, h)):
                x += 1
        else:
            if x - 1 >= 0 and (j is None or not hits_tower(tower, i, x-1, y, h)):
                x -= 1
        k += 1
        hit = False
        if (y - h) == 0 or hits_tower(tower, i, x, y-1, h):
            tower.append((y, x, i))
            tower.sort(key=lambda x: x[0], reverse=True)

            # search back
            if order:
                for oc in range(1, len(order)):
                    oi = len(order) - oc
                    oo = order[oi]
                    if oo[1] == x and oo[2] == i:
                        oip = oi - oc
                        if oip < 0: break
                        ooo = order[oip]
                        if oip > 0 and ooo[1] == x and ooo[2] == i:
                            for a, b in zip(order[oip:oi], order[oi:]):
                                if a[1] != b[1] or a[2] != b[2]: break
                            else:
                                flag = True
                            break
                if flag: break
            order.append((y, x, i))
            break
        if flag: break
        y -= 1

assert flag

delta_order_y = [y - order[oip][0] for y, _, _ in order[oip+1:oi]]

dy = order[oi][0] - order[oip][0]
r = 1000000000000 - oip - 1
big_y = dy * (r // (oi - oip)) + order[oip][0]
r_small = r % (oi - oip)
print(max(big_y + y for y in delta_order_y[:r_small]))
