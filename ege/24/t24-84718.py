from re import *

s = open('t24-84718.txt').read()

s = 'QXXXQ12Q34Q56QQ777WW77777HQQQ'

r = r'(?=([A-Z](?:[0-9]+[A-Z]+?){3}))'

R = findall(r, s)
print(R)
print(len(min(R, key=len)))
