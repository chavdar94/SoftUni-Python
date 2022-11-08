from collections import deque

main_colors = ('red', 'yellow', 'blue')
secondary_colors = ("orange", "purple", "green")

colors_combinations = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue'),
}

colors = []

words = deque(input().split())

while words:
    first = words.popleft()
    last = words.pop() if words else ''

    result = first + last
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    result = last + first
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        words.insert(len(words) // 2, first)
    if last:
        words.insert(len(words) // 2, last)
last
result_colors = []

for color in colors:
    if color in main_colors:
        result_colors.append(color)
        continue
    else:
        for secondary, combination in colors_combinations.items():
            col_1, col_2 = combination
            if col_1 in colors and col_2 in colors and secondary == color:
                result_colors.append(color)

print(result_colors)
