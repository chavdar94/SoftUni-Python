n = int(input())

longest_intersection = set()

for _ in range(n):
    left_side, right_side = input().split('-')
    left_start, left_end = left_side.split(',')
    right_start, right_end = right_side.split(',')
    left_set = set(range(int(left_start), int(left_end) + 1))
    right_set = set(range(int(right_start), int(right_end) + 1))

    current_intersection = left_set.intersection(right_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

str_intersection = [str(s) for s in longest_intersection]
print(f'Longest intersection is [{", ".join(str_intersection)}] with length {len(longest_intersection)}')
