students = {}
searched_course = None

while True:
    student = input()
    if ":" not in student:
        searched_course = student
        break

    data = student.split(":")
    name = data[0]
    student_id = data[1]
    course = data[2]

    if course not in students.keys():
        students[course] = {}

    students[course][student_id] = name

searched_course = searched_course.replace("_", " ")

for id in students[searched_course]:
    print(f"{students[searched_course][id]} - {id}")
