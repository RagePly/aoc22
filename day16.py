"""
from queue import PriorityQueue
with open("input/day16.txt", "r") as f:
    nodes = {}
    for line in f.readlines():
        tokens = line.split(maxsplit=9)
        p = tokens[1]
        r = int(tokens[4].split("=")[1][:-1])
        o = tokens[-1].strip().split(", ")
        
        nodes.update({
            p: {"rate": r, "leads": o}
        })


def find_rate(a, s, t, n, np, cost, visited):
    children = []
    for c in n[s]["leads"]:
        if c in visited: continue
        if c == t:
            np[a] = np.get(a, []) + [(c, cost + 1, n[t]["rate"])]
            return
        else:
            children.append(c)
    
    visited.add(s)
    for c in children:
        find_rate(a, c, t, n, np, cost + 1, visited)

new_nodes = {}
for (s, e) in ((l, r) for (i, l) in enumerate(nodes.keys()) for (j, r) in enumerate(nodes.keys()) if i != j):
    if nodes[e]["rate"] > 0:
        find_rate(s, s, e, nodes, new_nodes, 0, set())

q = PriorityQueue()
rt = 29 if nodes["AA"]["rate"] > 0 else 30
ss = rt * nodes["AA"]["rate"]

nodes = new_nodes
q.put((-ss, "AA", rt, set(), ss))
scores = {}
while not q.empty():
    _, n, t, v, ts = q.get()
    assert ts >= 0
    
    v.add(n)
    flag = True
    for c, cost, r in nodes[n]:
        if c in v: continue
        
        rem_time = t - cost - 1
        if rem_time < 0: continue

        new_score = rem_time * r
        tot_score = ts + new_score
        flag = False
        q.put((-new_score, c, rem_time, set(v), tot_score))
        if tot_score > scores.get(c, -9999):
            scores[c] = tot_score

print(max(scores.values()))
"""

# part 2
from queue import PriorityQueue
with open("input/day16.txt", "r") as f:
    nodes = {}
    for line in f.readlines():
        tokens = line.split(maxsplit=9)
        p = tokens[1]
        r = int(tokens[4].split("=")[1][:-1])
        o = tokens[-1].strip().split(", ")
        
        nodes.update({
            p: {"rate": r, "leads": o}
        })


def find_rate(a, s, t, n, np, cost, visited):
    children = []
    for c in n[s]["leads"]:
        if c in visited: continue
        if c == t:
            np[a] = np.get(a, []) + [(c, cost + 1, n[t]["rate"])]
            return
        else:
            children.append(c)
    
    visited.add(s)
    for c in children:
        find_rate(a, c, t, n, np, cost + 1, visited)

new_nodes = {}
for (s, e) in ((l, r) for (i, l) in enumerate(nodes.keys()) for (j, r) in enumerate(nodes.keys()) if i != j):
    if nodes[e]["rate"] > 0:
        find_rate(s, s, e, nodes, new_nodes, 0, set())

q = PriorityQueue()
rt = 29 if nodes["AA"]["rate"] > 0 else 30
ss = rt * nodes["AA"]["rate"]

nodes = new_nodes
q.put((-ss, "AA", rt, set(), ss))
scores = {}
while not q.empty():
    _, me, elephant, t, v, ts = q.get()
    assert ts >= 0
    
    v.add()
    possible_paths = []
    for (c_m, cost_m, r_m), (c_e, cost_e, r_e) in ((m, e) for m, e in zip(nodes[me], nodes[elephant]) if m[0]!=e[0]):
        if c_m in v or c_e in v: continue
        
        rem_time = t - cost - 1
        if rem_time < 0: continue

        new_score = rem_time * r
        tot_score = ts + new_score
        q.put((-new_score, c, rem_time, set(v), tot_score))
        if tot_score > scores.get(c, -9999):
            scores[c] = tot_score

print(max(scores.values()))