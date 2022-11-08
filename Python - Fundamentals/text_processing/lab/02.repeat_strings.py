words = input().split()
print(''.join([s * len(s) for s in words]))