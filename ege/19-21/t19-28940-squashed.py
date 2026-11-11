# 28940 Все ветви кода объединены всего в две;
# Та самая комбинация any/any + any/all, как в лучших видеоразборах
def vic(s):
    return s >= 124

def go(s, moves_left):
    moves = [s + 1, s + 5, s * 3]

    if moves_left % 2 != 0:
        if any(vic(ss) for ss in moves):
            return True
        if moves_left == 1:
            return False
        return any(go(ss, moves_left - 1) for ss in moves)
    else:
        if any(vic(ss) for ss in moves):
            return False # Четный ход никогда не должен выиграть; Это всегда тот игрок, который должен проиграть
        return all(go(ss, moves_left - 1) for ss in moves)

print('19:')
for s in range(1, 123):
    if go(s, 2):
        print('yep:', s)

print('20:')
for s in range(1, 123):
    if go(s, 3) and not go(s, 1):
        print('yep:', s)

print('21:')
for s in range(1, 123):
    if go(s, 4):
        print('yep:', s)
