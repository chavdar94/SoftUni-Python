from collections import deque


kids = deque(input().split())
toss = int(input())

toss_count = 0
while len(kids) > 1:
    toss_count += 1
    
    kid = kids.popleft()
    if toss_count < toss:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        toss_count = 0
print(f'Last is {kids.popleft()}')