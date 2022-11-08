def check_lesson(lesson):
    if lesson in courses:
        return True
    return False


def find_index(lesson):
    return courses.index(lesson)


def check_exercise(index):
    for i, course in enumerate(courses[index:]):
        if i == 1 and 'Exercise' in course:
            return True
        if i == 2:
            return False
    return False


def add(lesson):
    if not check_lesson(lesson):
        courses.append(lesson)


def insert(lesson, index):
    if not check_lesson(lesson):
        courses.insert(index, lesson)


def remove(lesson):
    if check_lesson(lesson):
        index_lesson = find_index(lesson)
        del courses[index_lesson]
        if check_exercise(index_lesson):
            del courses[index_lesson]


def swap(lesson_one, lesson_two):
    if check_lesson(lesson_one) and check_lesson(lesson_two):
        lesson_one_index = find_index(lesson_one)
        lesson_two_index = find_index(lesson_two)
        lesson_one_exercise = check_exercise(lesson_one_index)
        lesson_two_exercise = check_exercise(lesson_two_index)
        if lesson_one_exercise and lesson_two_exercise:
            lesson_one_exercise = courses[lesson_one_index + 1]
            courses[lesson_two_index + 1] = courses[lesson_two_index + 1]
            courses[lesson_two_index + 1] = lesson_one_exercise
        elif lesson_one_exercise:
            lesson_one_exercise = courses.pop(lesson_one_index + 1)
            courses.insert(find_index(lesson_two) + 1, lesson_one_exercise)
        elif lesson_two_exercise:
            lesson_two_exercise = courses.pop(lesson_two_index + 1)
            courses.insert(find_index(lesson_one) + 1, lesson_two_exercise)
        lesson_one_index = find_index(lesson_one)
        lesson_two_index = find_index(lesson_two)
        courses[lesson_one_index] = lesson_two
        courses[lesson_two_index] = lesson_one


def exercise(lesson):
    if check_lesson(lesson):
        lesson_index = find_index(lesson)
        if not check_exercise(lesson_index):
            courses.insert(lesson_index + 1, f'{lesson}-Exercise')
    else:
        courses.append(lesson)
        courses.append(f'{lesson}-Exercise')


courses = input().split(', ')

while True:
    command = input()
    if command == "course start":
        break
    commands = command.split(':')
    task = commands[0]
    course = commands[1]
    if task == "Add":
        add(course)
    elif task == "Insert":
        index = int(commands[2])
        insert(course, index)
    elif task == "Remove":
        remove(course)
    elif task == "Swap":
        lesson_one_name = course
        lesson_two_name = commands[2]
        swap(lesson_one_name, lesson_two_name)
    elif task == "Exercise":
        exercise(course)

for index, name in enumerate(courses, 1):
    print(f'{index}.{name}')
