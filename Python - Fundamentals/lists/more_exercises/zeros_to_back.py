numbers_list = list(map(int, input().split(", ")))

zeros_counter = numbers_list.count(0)

for number in numbers_list:
    if "0" in numbers_list:
        numbers_list.remove(0)

for insert in range(zeros_counter):
    numbers_list.append(0)

print(numbers_list)