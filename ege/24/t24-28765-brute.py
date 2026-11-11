with open('t24-28765.txt', 'rt') as f:
    S = f.read()

# VERY slow (30-40 min run time)
N = 180
maxs = ''
for i in range(len(S)):
    for j in range(i + len(maxs), len(S) + 1):
        if S[i:j].count('BC') <= 180:
            maxs = S[i:j]
            if len(maxs) > 35000:
                print(i, len(maxs))
        else:
            break

print(maxs, len(maxs))
