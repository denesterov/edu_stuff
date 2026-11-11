# 28940.20 отращиваем код от 19

def vic(s):
    return s >= 124

def go(s, moves_left):
    moves = [s + 1, s + 5, s * 3]

    if moves_left == 1:
        return any(vic(ss) for ss in moves)

    if moves_left == 2:
        if any(vic(ss) for ss in moves): # Вова не должен выиграть ни при каком раскладе
            return False
        return all(go(ss, moves_left - 1) for ss in moves)

    if moves_left == 3:
        if any(vic(ss) for ss in moves):
            return True # Вообще-то, Петя не может выиграть за один ход; но так тут сделано для общности
        return any(go(ss, moves_left - 1) for ss in moves)

print('20:')
for s in range(1, 123):
    if go(s, 3) and not go(s, 1):
        print(s)
