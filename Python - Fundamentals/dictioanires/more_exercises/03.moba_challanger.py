def add_player(dct, name, pos, points):
    if name not in dct:
        dct[name] = {}
    if pos not in dct[name]:
        dct[name][pos] = 0
    if dct[name][pos] < points:
        dct[name][pos] = points
    return dct


def battle(dct, player1, player2):
    if (player1 and player2) in dct:
        for p_one in dct[player1]:
            if p_one in dct[player2]:
                p_one_sum = sum(dct[player1].values())
                p_two_sum = sum(dct[player2].values())
                if p_one_sum > p_two_sum:
                    del dct[player2]
                elif p_one_sum < p_two_sum:
                    del dct[player1]
                break


players_pool = {}
players = []

player_info = input()
while player_info != 'Season end':
    if '->' in player_info:
        username, position, skill = [int(x) if x.isdigit() else x for x in player_info.split(' -> ')]
        add_player(players_pool, username, position, skill)
    elif 'vs' in player_info:
        player_one, player_two = player_info.split(" vs ")
        battle(players_pool, player_one, player_two)

    player_info = input()

for player_name in players_pool:
    players.append({'name': player_name, 'total_score': sum(players_pool[player_name].values())})

for player in sorted(players, key=lambda x: (-x['total_score'], x['name'])):
    print(f'{player["name"]}: {player["total_score"]} skill')
    for pos, score in sorted(players_pool[player['name']].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {pos} <::> {score}')
