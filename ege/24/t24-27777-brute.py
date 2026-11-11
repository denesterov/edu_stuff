# 27777
with open('t24-27777.txt', 'rt') as f:
    S = f.read()

D = '0123456789AB'

L = len(S)
maxstr = ''
i = 0
while i < L:
    if not S[i] in D:
        i += 1
        continue
    for j in range(i, L):
        if S[j] in D:
            c = S[i:j + 1]
            if len(c) > len(maxstr):
                maxstr = c
        else:
            i = j
            break

print(len(maxstr), maxstr)
