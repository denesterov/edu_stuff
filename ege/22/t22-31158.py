# 31158
P = {id: (dur, deps) for id, dur, *deps in [[int(s) for s in ln.split()] for ln in open('t22-31158.txt')]}

def build(id, res: set):
    if id == 0:
        return 0
    dur, deps = P[id]
    max_dep_dur = max([build(d, res) for d in deps] + [0])
    if dur + max_dep_dur <= 21:
        res.add(id)
    return dur + max_dep_dur

res = set()
for id in P.keys():
    build(id, res)

print(len(res))
