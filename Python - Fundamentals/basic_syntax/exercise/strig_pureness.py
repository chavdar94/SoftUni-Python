n = int(input())

for i in range(n):
    data = input()
    if "," in data or "." in data or "_" in data:
        print(f"{data} is not pure!")
    else:
        print(f"{data} is pure.")