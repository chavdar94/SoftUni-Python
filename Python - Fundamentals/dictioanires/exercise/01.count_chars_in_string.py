data = input()
chars = {}
for i in data:
    if i not in chars and i != " ":
        chars[i] = 0
    if i != " ":
        chars[i] += 1
for key,value in chars.items():
    print(f"{key} -> {value}")
