with open('t24-28765.txt', 'rt') as f:
    S = f.read()

N = 180
beg, end = 0, 0
count = 0
maxs = ''
while True:
    if end >= len(S) and count <= N:
        break
    if end < len(S) and count <= N:
        end += 1
        if S[end - 2 : end] == 'BC':
            count += 1
        if count <= N and len(maxs) < end - beg:
            maxs = S[beg:end]
    elif count > N:
        if S[beg : beg + 2] == 'BC':
            count -= 1
        beg += 1

print(maxs, len(maxs))
