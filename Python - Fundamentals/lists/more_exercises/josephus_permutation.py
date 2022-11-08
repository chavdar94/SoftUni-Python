people = input().split()
step = int(input())
executed_people = []
index = 0

while len(people) > 0:
    index = (index + step - 1) % len(people)
    executed_people.append(people.pop(index))
print(f"[{','.join(executed_people)}]")
