# 28940.19 простейшая форма

def vic(s):
    return s >= 124

def go(s, moves_left):
    moves = [s + 1, s + 5, s * 3]

    if moves_left == 1:
        return any(vic(ss) for ss in moves)

    if moves_left == 2:
        if any(vic(ss) for ss in moves):
            return False
        return all(go(ss, moves_left - 1) for ss in moves)

print('19:')
for s in range(1, 123):
    if go(s, 2):
        print(s)
