number_of_inputs = int(input())
key_word = input()

list_of_inputs = []
for string in range(number_of_inputs):
    current_string = input()
    list_of_inputs.append(current_string)

print(list_of_inputs)

filtered_inputs = []
for key in list_of_inputs:
    if key_word in key:
        filtered_inputs.append(key)
print(filtered_inputs)