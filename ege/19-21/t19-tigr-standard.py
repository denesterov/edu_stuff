# 21418 - 21420

def play(S, moves_left):
    avail_moves = [S - 2, S // 2]

    if moves_left % 2 == 1:
        if any(s <= 87 for s in avail_moves):
            return True
        if moves_left > 1:
            return any(play(s, moves_left - 1) for s in avail_moves)
    else:
        if any(s <= 87 for s in avail_moves):
            return False
        return all(play(s, moves_left - 1) for s in avail_moves)
    return False

for S in range(89, 200):
    if play(S, 2):
        print('19. S=', S)

for S in range(89, 200):
    if play(S, 3) and not play(S, 1):
        print('20. S=', S)

for S in range(89, 200):
    if play(S, 4) and not play(S, 2):
        print('21. S=', S)
