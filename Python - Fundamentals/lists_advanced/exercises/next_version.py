old_version = list(map(int, input().split(".")))
new_version = []

old_version[2] += 1
if old_version[2] < 10:
    new_version = old_version
elif old_version[2] >= 10:
    old_version[2] = 0
    old_version[1] += 1
    new_version = old_version
    if old_version[1] >= 10:
        old_version[1] = 0
        old_version[0] += 1
        new_version = old_version
new_version = list(map(str,new_version))
print('.'.join(new_version))
