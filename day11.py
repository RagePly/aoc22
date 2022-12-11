from operator import add, mul
from functools import reduce
with open("input/day11.txt", "r") as f:
    monkeys = []
    for monkey in f.read().strip().split("\n\n"):
        _, s, op, test, t, f = monkey.split("\n")
        
        _, op, rhs = op.split("=")[1].strip().split()

        m = {
            "items": list(map(int, s.split(":")[1].strip().split(", "))),
            "operator": add if op == "+" else mul,
            "argument": None if rhs == "old" else int(rhs),
            "test": int(test.split()[-1]),
            "true": int(t.split()[-1]),
            "false": int(f.split()[-1]),
            "inspect": 0
        }
        monkeys.append(m)

for _ in range(20):
    for i in range(len(monkeys)):
        m = monkeys[i]
        for item in m["items"]:
            rhs = item if (x := m["argument"]) is None else x
            wl = m["operator"](item, rhs) // 3
            if wl % m["test"] == 0:
                monkeys[m["true"]]["items"].append(wl)
            else:
                monkeys[m["false"]]["items"].append(wl)
            
            m["inspect"] += 1
        m["items"] = []

monkey_business = reduce(mul, sorted(map(lambda m: m["inspect"], monkeys))[-2:])
print(monkey_business)

from operator import add, mul
from functools import reduce
from math import lcm
with open("input/day11.txt", "r") as f:
    monkeys = []
    tests = []
    for monkey in f.read().strip().split("\n\n"):
        _, s, op, test, t, f = monkey.split("\n")
        test = int(test.split()[-1])
        tests.append(test)
        _, op, rhs = op.split("=")[1].strip().split()

        m = {
            "items": list(map(int, s.split(":")[1].strip().split(", "))),
            "operator": add if op == "+" else mul,
            "argument": None if rhs == "old" else int(rhs),
            "test": test,
            "true": int(t.split()[-1]),
            "false": int(f.split()[-1]),
            "inspect": 0
        }
        monkeys.append(m)
    mod = lcm(*tests)

for r in range(10000):
    for i in range(len(monkeys)):
        m = monkeys[i]
        for item in m["items"]:
            rhs = item if (x := m["argument"]) is None else x
            wl = m["operator"](item, rhs) % mod
            if wl % m["test"] == 0:
                monkeys[m["true"]]["items"].append(wl)
            else:
                monkeys[m["false"]]["items"].append(wl)
            m["inspect"] += 1
        m["items"] = []


monkey_business = reduce(mul, sorted(map(lambda m: m["inspect"], monkeys))[-2:])
print(monkey_business)