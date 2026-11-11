with open('t24-27634.txt', 'rt') as f:
    S = f.read()

M = 270
L = len(S)
begin, end = 0, 0
cnt = 0

substr = None

while True:
    if cnt < M and end < L:
        # двигаем вперед окончание строки, считаем количество прибывших Z
        if S[end] == 'Z':
            cnt += 1
        end += 1

    if cnt >= M: # Если выполнено условие на количество Z, двигаем начало строки вперед
        if substr is None or end - begin < len(substr):
            substr = S[begin:end] # но сначала проверим, не нашли ли наименьшую строку
        if begin < end:
            if S[begin] == 'Z':
                cnt -= 1
            begin += 1

    if end == L and cnt < M:
        break

print(substr, len(substr))
