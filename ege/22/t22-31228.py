# 31228
P = {}
for id, dur, *deps in [[int(s) for s in ln.split()] for ln in open('t22-31228.txt')]:
    P[id] = (dur, [] if deps == [0] else deps)

def foo(id, res: set):
    dur, deps = P[id]
    dep_dur = max([foo(d, res) for d in deps] + [0])
    if dep_dur <= 26 <= dur + dep_dur:
        res.add(id)
    return dur + dep_dur

res = set()
for id in P.keys():
    foo(id, res)

print(len(res))
