contests = {}

# adding contests
current_contest = input()
while current_contest != 'end of contests':
    current_contest = current_contest.split(':')
    contest_name = current_contest[0]
    contest_password = current_contest[1]
    contests[contest_name] = contest_password
    current_contest = input()

#  adding contest users if the contest name and password are valid
user_info = input()
students = {}
while user_info != 'end of submissions':
    user_info = user_info.split('=>')

    contest_name = user_info[0]
    contest_password = user_info[1]
    user_name = user_info[2]
    user_points = int(user_info[3])

    if contest_name in contests and contest_password == contests[contest_name]:
        students[user_name] = students.get(user_name, {})
        students[user_name][contest_name] = students[user_name].get(contest_name, 0)
        if students[user_name][contest_name] < user_points:
            students[user_name][contest_name] = user_points

    user_info = input()

#  finding the best user
best_name = ''
best_points = 0

for name in students:
    max_points = sum(students[name].values())
    if max_points > best_points:
        best_name = name
        best_points = max_points
print(f'Best candidate is {best_name} with total {best_points} points.')
print('Ranking:')

for name in sorted(students):
    print(name)
    for course_name, points in sorted(students[name].items(), key=lambda x: -x[1]):
        print(f"#  {course_name} -> {points}")
