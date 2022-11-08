number = int(input())

for num in range(1,number+1):
    sum_of_nums = 0
    digits = num
    while digits > 0:
        sum_of_nums += digits % 10
        digits = digits // 10
    if sum_of_nums == 5 or sum_of_nums == 7 or sum_of_nums == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
