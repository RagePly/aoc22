# part 1
with open("input/day7.txt") as f:
    cd = []
    tree = {}
    for line in map(str.strip, f.readlines()):
        if line.startswith("$"):
            _, com, *arg = line.split()
            if com == "cd":
                match arg[0]:
                    case "..":
                        cd.pop()
                    case "/":
                        cd.clear()
                    case d:
                        cd.append(d)
        else:
            _dir = tree
            for d in cd:
                _dir = _dir[d]
            a, b = line.split()
            if a == "dir":
                _dir[b] = {}
            else:
                _dir[b] = a

def find(tree, a):
    s = 0
    for c in tree.values():
        if isinstance(c, dict):
            s += find(c, a)
        else:
            s += int(c)
    if s <= 100000:
        a.append(s)
    
    return s
a = []
find(tree, a)

print(sum(a))

# part 2
with open("input/day7.txt") as f:
    cd = []
    tree = {} 
    for line in map(str.strip, f.readlines()):
        if line.startswith("$"):
            _, com, *arg = line.split()
            if com == "cd":
                match arg[0]:
                    case "..":
                        cd.pop()
                    case "/":
                        cd.clear()
                    case d:
                        cd.append(d)
        else:
            _dir = tree
            for d in cd:
                _dir = _dir[d]
            a, b = line.split()
            if a == "dir":
                _dir[b] = {}
            else:
                _dir[b] = a

def find(tree, a):
    s = 0
    for c in tree.values():
        if isinstance(c, dict):
            s += find(c, a)
        else:
            s += int(c)
    a.append(s)
    return s
a = []
find(tree, a)

a.sort()
space = 70000000 - a[-1]
a = filter(lambda s: space + s >= 30000000, a)
print(next(a))
