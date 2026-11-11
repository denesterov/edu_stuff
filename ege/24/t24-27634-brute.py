with open('t24-27634.txt', 'rt') as f:
    S = f.read()

M = 270

substr = None

minl = 3000
for l in range(len(S)):
    for r in range(l + 1, l + minl):
        c = S[l:r]
        if c.count('Z') >= 270 and len(c) < minl:
            substr = c
            minl = len(c)

print(S)
print(minl)