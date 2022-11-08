employees = input().split()
factor = int(input())

employees_happiness = list(map(lambda x: int(x) * factor, employees))
average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_count = 0
employee_count = 0

for employee in employees_happiness:
    if employee >= average_happiness:
        happy_count += 1
    employee_count += 1

if happy_count >= len(employees_happiness) / 2:
    print(f'Score: {happy_count}/{employee_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{employee_count}. Employees are not happy!')