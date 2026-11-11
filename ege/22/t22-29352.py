# 29352
P = {}
for id, dur, *deps in [[int(s) for s in ln.split()] for ln in open('t22-29352.txt')]:
    P[id] = (dur, deps)

def foo(id):
    dur, deps = P[id]
    dep_dur = 0 if deps == [] else max(foo(d) for d in deps)
    return dur + dep_dur

print(max(foo(pid) for pid in P.keys()))
