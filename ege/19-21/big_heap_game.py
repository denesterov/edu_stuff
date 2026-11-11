# Ancient code, Jan 2026

PLAYER_A = 'P'
PLAYER_B = 'V'

game_finished = lambda S: S <= 30

actions = [
    lambda S: S // 4,
    lambda S: S - 3,
    lambda S: S - 5
]

def switch_player(player):
    return PLAYER_A if player == PLAYER_B else PLAYER_B


trajectries = []

def save_trajectory(trajectory, winner):
    trajectries.append((winner, [tup for tup in trajectory]))

def make_all_moves(S, player, trajectory, move_limit):
    for act in actions:
        SS = act(S)
        trajectory.append((player, SS, SS - S))
        if game_finished(SS):
            save_trajectory(trajectory, player)
        elif move_limit >= 0:
            make_all_moves(SS, switch_player(player), trajectory, move_limit - 1)
        trajectory.pop()


def brute_force():
    make_all_moves(124, PLAYER_A, [], 2)
    score = {}
    for winner, traj in trajectries:
        score[winner] = score.get(winner, 0) + 1
        print(f'The winner is {winner}: {traj}')
    print(f'Scores: {score}')

brute_force()



def try_moves(S, player, moves_left):
    if moves_left <= 0 and not game_finished(S):
        return None
    
    other_player = switch_player(player)

    if game_finished(S):
        return other_player
    
    wins = 0
    defeats = 0
    for act in actions:
        new_S = act(S)
        result = try_moves(new_S, other_player, moves_left - 1)
        if result == None:
            break
        if result == player:
            wins += 1
        else:
            defeats += 1

    player_is_favorite = (moves_left % 2) == 1
    if player_is_favorite:
        if wins == len():

    if wins == len(actions):
        return player
    if defeats == len(actions):
        return other_player
    return None


for S in range(31, 200):
    winner = try_moves(S, PLAYER_A, 1)
    if winner == PLAYER_B:
        print(f'Result: {S=}')
