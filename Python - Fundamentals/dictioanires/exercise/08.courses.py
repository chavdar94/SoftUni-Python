courses = {}

command = input()
while command != 'end':
    course_info = command.split(' : ')
    course = course_info[0]
    student_name = course_info[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student_name)

    command = input()

for key in courses:
    print(f"{key}: {len(courses[key])}")
    for student in courses[key]:
        print(f"-- {student}")