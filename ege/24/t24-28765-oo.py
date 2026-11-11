s = open('t24-28765.txt').read()


# s = 'BC111BC23BC23BC88888BC555555555555555555555'

N = 180 # 180

c = ''
k = 0
m = 0
ms = ''

for r in range(len(s)):
    c += s[r]
    if c[-2:] == 'BC':
        k += 1
    while k > N:
        if c[:2] == 'BC':
            k -= 1
        c = c[1:]
    if len(c) > m:
        m = len(c)
        ms = c
print(ms, m)
