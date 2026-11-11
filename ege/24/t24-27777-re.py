# 27777
import re

s = open('t24-27777.txt').read()

r = re.findall(r'(?:[1-9AB]+[0-9AB]*)', s)
# print(len(r), r)
m = max(r, key=len)
print(m, len(m))
