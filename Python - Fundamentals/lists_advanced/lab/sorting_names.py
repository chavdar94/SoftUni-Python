names = input().split(", ")

sorted_names = sorted(names, key=lambda x: (-len(x), x))
print(sorted_names)