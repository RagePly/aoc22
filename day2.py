# part 1
with open("input/day2.txt", "r") as f:
    points = 0
    for op, me in map(str.split, f.readlines()):
        op = "ABC".index(op)
        me = "XYZ".index(me)

        points += me + 1
        if op == me:
            points += 3
        elif (op + 1) % 3 == me:
            points += 6

print(points)

# part 2
with open("input/day2.txt", "r") as f:
    points = 0
    for op, me in map(str.split, f.readlines()):
        op = "ABC".index(op)

        if me == "X":
            points += (op - 1) % 3 + 1
        elif me == "Y":
            points += 3 + op + 1
        else:
            points += 6 + (op + 1) % 3 + 1

print(points)
