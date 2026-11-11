import re
s = open('t24-24895.txt').read()
# s = s[:1000]

# r = re.findall(r'(?=((?:[1-9][0-9]*)(?:[\+\*](?:[1-9][0-9]*)){,39}))', s)
r = re.findall(r'(?=([1-9]+(?:[+*][1-9]+){,39}))', s)

m = max(r, key=len)
print(m)
print(len(m))
