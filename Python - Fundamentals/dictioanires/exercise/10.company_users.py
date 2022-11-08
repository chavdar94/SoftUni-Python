companies = {}

command = input()
while command != 'End':

    information = command.split(' -> ')
    company_name = information[0]
    employee_id = information[1]
    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(employee_id)
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

    command = input()

for key, value in companies.items():
    print(key)
    for id in value:
        print(f"-- {id}")
