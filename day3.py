# part 1
with open("input/day3.txt", "r") as f:
    s = 0
    for line in map(str.strip, f.readlines()):
        l, r = set(line[:len(line)//2]), set(line[len(line)//2:])
        d = ord((l & r).pop())
        s += (d - ord('a') + 1) if d >= ord('a') else (d - ord("A") + 27)

print(s)

# part 2
import itertools
with open("input/day3.txt", "r") as f:
    s = 0
    it = map(str.strip, f.readlines())
    while (es := list(itertools.islice(it, 3))):
        e1, e2, e3 = es
        c = set(e1) & set(e2) & set(e3)
        d = ord(c.pop())
        s += (d - ord('a') + 1) if d >= ord('a') else (d - ord("A") + 27)

print(s)