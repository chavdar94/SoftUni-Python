sums_list = input().split(", ")
number_beggars = int(input())

sums_of_beggars = []
current_beggar = 0
beggar_sum = 0

while current_beggar < number_beggars:
    for beggar in range(current_beggar, len(sums_list), number_beggars):
        beggar_sum += int(sums_list[beggar])
    sums_of_beggars.append(beggar_sum)
    beggar_sum = 0
    current_beggar += 1
print(sums_of_beggars)