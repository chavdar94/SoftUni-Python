number_of_students = int(input())

students_dict = {}
for student in range(number_of_students):
    name, grade = input().split()
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for student, grades in students_dict.items():
    grades_list = [str(f"{grade:.2f}") for grade in grades]
    average = sum(grades) / len(grades)
    print(f'{student} -> {" ".join(grades_list)} (avg: {average:.2f})')