# part 1
with open("input/day1.txt", "r") as f:
    data = max(map(lambda l: sum(map(int, l.split("\n"))), f.read().strip().split("\n\n")))

print(data)

# part 2
with open("input/day1.txt", "r") as f:
    data = sorted(map(lambda l: sum(map(int, l.split("\n"))), f.read().strip().split("\n\n")))

print(sum(data[-3:]))