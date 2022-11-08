judge = {}
users = {}
data = input()
while data != 'no more time':
    username, contest, points = data.split(' -> ')
    points = int(points)

    judge[contest] = judge.get(contest, {})
    judge[contest][username] = judge[contest].get(username, 0)
    users[username] = users.get(username, 0)

    if users[username] in users and users[username] == points:
        users[username] += points

    if judge[contest][username] < points:
        users[username] += points - judge[contest][username]
        judge[contest][username] = points

    data = input()

for current_contest in judge.keys():
    print(f'{current_contest}: {len(judge[current_contest])} participants')
    for pos, (user, points) in enumerate(sorted(judge[current_contest].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f'{pos}. {user} <::> {points}')

print('Individual standings:')
for pos, (user, points,) in enumerate(sorted(users.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f'{pos}. {user} -> {points}')