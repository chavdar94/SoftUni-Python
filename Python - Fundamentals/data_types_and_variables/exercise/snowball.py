number_of_snowballs = int(input())

max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_snowball_value = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
        max_snowball_value = snowball_value

print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")