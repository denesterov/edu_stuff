with open('t24-26551.txt','rt') as f:
    S = f.read()

beg, end = 0, 0
mx = 0
maxs = ''

DIG = '0123456789ABCD'
ODD = '02468AC'

while end < len(S):
    if S[end] in DIG:
        end += 1
        if S[end-1] in ODD:
            n = int(S[beg:end], base=14)
            if n > mx:
                mx = n
                maxs = S[beg:end]
    else:
        beg, end = end + 1, end + 1

print(maxs.lstrip('0'))
print(len(maxs.lstrip('0')))
print(mx)
