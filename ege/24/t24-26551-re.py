import re

s = open('t24-26551.txt').read()
# s = s[10000:11000]

r = re.findall(r'(?:[1-9A-D][0-9A-D]*[02468AC])', s)
m = max(r, key=lambda s: int(s, 14))

print(m)
print(len(m))
