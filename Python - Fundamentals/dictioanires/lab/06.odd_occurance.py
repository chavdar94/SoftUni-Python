data = input().split()
data_dict = {}

for current_data in data:
    data_lower = current_data.lower()
    if data_lower not in data_dict:
        data_dict[data_lower] = 0
    data_dict[data_lower] += 1

for key, value in data_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
