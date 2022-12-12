# part 1
from aoctools.datastruct import vec, fgraph
from aoctools.algorithms import A_star

with open("input/day12.txt", "r") as f:
    grid = [list(l.strip()) for l in f.readlines()]

height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        z = grid[y][x]
        if z == "S":
            start = vec(x, y)
            z = "a"
        elif z == "E":
            end = vec(x, y)
            z = "z"
        
        grid[y][x] = ord(z) - ord('a')
    
def children(pos: vec):
    global height, width, grid
    moves = []
    for d in pos.cardinal(2):
        p = pos + d
        x, y = p
        if 0 <= x < width and 0 <= y < height:
            z0 = grid[pos[1]][pos[0]]
            z1 = grid[y][x]
            if z1 <= z0 or z1 == z0 + 1:
                moves.append((p, 1))
    return moves
    
            

graph = fgraph(children)
_, steps = A_star(graph, start, end, vec.manhattan_betweeen)
print(steps)

# part 2 (bruh slow af)
from aoctools.datastruct import vec, fgraph
from aoctools.algorithms import A_star

with open("input/day12.txt", "r") as f:
    grid = [list(l.strip()) for l in f.readlines()]

height = len(grid)
width = len(grid[0])
starts = []
for y in range(height):
    for x in range(width):
        z = grid[y][x]
        if z == "S":
            z = "a"
        elif z == "E":
            end = vec(x, y)
            z = "z"
        
        if z == 'a':
            starts.append(vec(x, y))
        grid[y][x] = ord(z) - ord('a')
    
def children(pos: vec):
    global height, width, grid
    moves = []
    for d in pos.cardinal(2):
        p = pos + d
        x, y = p
        if 0 <= x < width and 0 <= y < height:
            z0 = grid[pos[1]][pos[0]]
            z1 = grid[y][x]
            if z1 <= z0 or z1 == z0 + 1:
                moves.append((p, 1))
    return moves

graph = fgraph(children)
minsteps = 10000000000000000000
for start in starts:
    res = A_star(graph, start, end, vec.manhattan_betweeen)
    if res is not None:
        minsteps = min(res[1], minsteps)

print(minsteps)