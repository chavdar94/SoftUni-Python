clothes = list(map(int, input().split()))
rack_capacity = int(input())

racks = 1
current_capacity = rack_capacity

while clothes:
    current_cloth = clothes[-1]
    if current_cloth > current_capacity:
        racks += 1
        current_capacity = rack_capacity
    else:
        current_capacity -= current_cloth
        clothes.pop()

print(racks)
