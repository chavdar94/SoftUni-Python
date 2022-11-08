first_list = input().split(", ")
second_list = input().split(", ")
final_list = []

for item in first_list:
    for new_item in second_list:
        if item in new_item:
            final_list.append(item)
final_list = list(dict.fromkeys(final_list))
print(final_list)