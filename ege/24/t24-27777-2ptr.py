# 27777
with open('t24-27777.txt', 'rt') as f:
    S = f.read()

D = '0123456789AB'
L = len(S)
begin, end = 0, 0

substr = None

while end < L:
    if S[end] in D:
        end += 1

        if substr is None or end - begin > len(substr):
            substr = S[begin:end]
    else:
        # начинаем поиск с начала, с позиции после end
        begin = end + 1
        end = begin

print(substr, len(substr))
