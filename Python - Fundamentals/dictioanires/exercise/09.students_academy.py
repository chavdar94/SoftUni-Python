number_of_students = int(input())

students = {}

for i in range(number_of_students):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

#  dictionary comprehension
passed_students = {key: value for (key,value) in students.items() if sum(value)/len(value) >= 4.5}

for key, value in passed_students.items():
    average = sum(value) / len(value)
    print(f"{key} -> {average:.2f}")

#  normal for loop
# passed_students = {}
#
# for key in students:
#     average = sum(students[key]) / len(students[key])
#     if average >= 4.5:
#         passed_students[key] = average
#
# for key, value in passed_students.items():
#     print(f"{key} -> {value:.2f}")
