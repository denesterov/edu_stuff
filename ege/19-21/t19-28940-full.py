def vic(s):
    return s >= 124

def go(s, moves_left):
    moves = [s + 1, s + 5, s * 3]

    if moves_left == 1:
        return any(vic(ss) for ss in moves)

    if moves_left == 2 or moves_left == 4:
        if any(vic(ss) for ss in moves):
            return False # Четный ход никогда не должен выиграть; Это всегда тот игрок, который должен проиграть
        return all(go(ss, moves_left - 1) for ss in moves)

    if moves_left == 3:
        if any(vic(ss) for ss in moves):
            return True
        return any(go(ss, moves_left - 1) for ss in moves)

print('19:')
for s in range(1, 123):
    if go(s, 2):
        print('yep:', s)

print('20:')
for s in range(1, 123):
    if go(s, 3):
        print('yep:', s)

print('21:')
for s in range(1, 123):
    if go(s, 4):
        print('yep:', s)
