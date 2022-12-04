# part 1 (started ~18:04)
import re
with open("input/day4.txt") as f:
    r = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    s = 0
    for m in re.finditer(r, f.read()):
        a, b, c, d = map(int, m.groups())
        if a <= c and d <= b:
            s += 1
        elif c <= a and b <= d:
            s += 1

print(s)

# part 2
import re
with open("input/day4.txt") as f:
    r = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    s = 0
    for m in re.finditer(r, f.read()):
        a, b, c, d = map(int, m.groups())
        lhs = max(a, c)
        rhs = min(b, d)
        if lhs <= rhs:
            s += 1

print(s)

# end 18:11:39