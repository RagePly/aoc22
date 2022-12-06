# part 1
with open("input/day6.txt") as f:
    data = f.read().strip()

for i in range(len(data)):
    if len(set(data[i:i+4])) == 4:
        print(i + 4)
        break


# part 2
with open("input/day6.txt") as f:
    data = f.read().strip()

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        print(i + 14)
        break