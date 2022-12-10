with open("input/day10.txt", "r") as f:
    instr = []
    for l in f.readlines():
        op, *arg = l.strip().split()
        if op == "addx":
            instr += [("noop",), (op, *map(int, arg))]
        else:
            instr.append((op,))

x = 1
tot = []
flag20 = True
for i, (op, *args) in enumerate(instr):
    j = i + 1
    if flag20 and j == 20:
        print(j, x, j * x)
        tot.append(j * x)
        flag20 = False
    elif not flag20 and (j + 20) % 40 == 0:
        print(j, x, j * x)
        tot.append(j * x)
    
    if op == "addx":
        x += args[0]

print(sum(tot))

with open("input/day10.txt", "r") as f:
    instr = []
    for l in f.readlines():
        op, *arg = l.strip().split()
        if op == "addx":
            instr += [("noop",), (op, *map(int, arg))]
        else:
            instr.append((op,))

x = 1
tot = []
buffer = []
for i, (op, *args) in enumerate(instr):
    pos = i % 40
    if x - 1 <= pos <= x + 1:
        buffer.append("##")
    else:
        buffer.append("  ")

    if op == "addx":
        x += args[0]

    if ((i+1) % 40) == 0:
        tot.append(buffer)
        buffer = []

print("\n".join("".join(l) for l in tot))