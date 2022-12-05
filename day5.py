# part 1
with open("input/day5.txt") as f:
    stacks, moves = map(str.rstrip, f.read().split("\n\n"))
    stacks = [[c[1:-1] for c in r.split(" ")] for r in stacks.split("\n")[:-1]]
    stack = [[] for _ in range(min(map(len, stacks)))]
    for s in stacks:
        s.reverse()
        i = 0
        while s:
            p = s.pop()
            if p:
                stack[i].append(p)
            else:
                s.pop()
                s.pop()
                s.pop()
            i += 1
    
    for s in stack:
        s.reverse()
    for m in moves.split("\n"):
        c, f, t = map(int, m.split(" ")[1::2])
        for _ in range(c):
            i = stack[f-1].pop()
            stack[t-1].append(i)
    for s in stack:
        if s:
            print(s[-1], end="")

print()

# part 2
with open("input/day5.txt") as f:
    stacks, moves = map(str.rstrip, f.read().split("\n\n"))
    stacks = [[c[1:-1] for c in r.split(" ")] for r in stacks.split("\n")[:-1]]
    stack = [[] for _ in range(min(map(len, stacks)))]
    for s in stacks:
        s.reverse()
        i = 0
        while s:
            p = s.pop()
            if p:
                stack[i].append(p)
            else:
                s.pop()
                s.pop()
                s.pop()
            i += 1
    
    for s in stack:
        s.reverse()
    for m in moves.split("\n"):
        c, f, t = map(int, m.split(" ")[1::2])
        i = stack[f-1][-c:]
        for _ in range(c):
            stack[f-1].pop()
        stack[t-1] += i
    for s in stack:
        if s:
            print(s[-1], end="")