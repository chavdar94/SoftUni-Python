from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]

boxes = 0

while eggs and papers:
    first_egg = eggs.popleft()
    last_paper = papers.pop()

    if first_egg <= 0:
        papers.append(last_paper)
        continue

    elif first_egg == 13:
        papers.append(last_paper)
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    if first_egg + last_paper <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(s) for s in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(s) for s in papers)}')
