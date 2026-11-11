from re import *

s = open('t24-85700.txt').read()
# s = 'TXXXTXXXTXXOXXOXTMMTSSTA'
# s = s[:100000]

# re = r'(?=((?:T[^AEIOUY]*?){3}[AEIOUY]))' # оставил для примера, это неактуальная регуля!
re = r'(?:T[^TAEIOUY]*){63,63}[AEIOUY]'
# [^ABC] - обратное множество, то есть любой символ, НЕ УКАЗАННЫЙ в скобках

R = findall(re, s)
# print(R)
M = min(R, key=len) if len(R) else ''
print(M, len(M))
