n = int(input())

names = set()
for _ in range(n):
    user_name = input()
    names.add(user_name)
[print(name) for name in names]