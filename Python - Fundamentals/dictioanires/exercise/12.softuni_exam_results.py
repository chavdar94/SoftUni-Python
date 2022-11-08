def add_student(dict, name, lang, score):
    if name not in dict:
        dict[name] = {'language': lang, 'points': 0}
    if score >= dict[name]['points']:
        dict[name]['points'] = score


def remove_student(dict, name):
    if name in dict:
        del dict[name]


def add_submission(dict, lang):
    if lang not in dict:
        dict[lang] = 0
    dict[lang] += 1


command = input()
students = {}
languages = {}

while command != "exam finished":
    if 'banned' in command:
        command = command.split('-')
        username = command[0]
        remove_student(students, username)
    else:
        username, language, points = command.split('-')
        add_student(students, username, language, int(points))
        add_submission(languages, language)

    command = input()

print('Results:')
for name, value in students.items():
    print(f'{name} | {students[name]["points"]}')

print('Submissions:')
for lang_name, submissions in languages.items():
    print(f'{lang_name} - {submissions}')
