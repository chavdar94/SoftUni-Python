numbers = input().split()
numbers_list = [int(i) for i in numbers]


def exchange(index, num_list):
    if int(index) >= len(num_list) or int(index) < 0:
        print("Invalid index")
        return num_list
    else:
        num_list = num_list[index + 1:] + num_list[: index + 1]
        return num_list


def max_even_odd(num_list):
    max_index = 0
    max_even = -2 ** 31
    is_found = False
    if command_list[1] == "even":
        for index, number in enumerate(num_list):
            if number >= max_even and number % 2 == 0:
                max_even = number
                max_index = index
                is_found = True
        if is_found:
            return max_index
        else:
            return "No matches"
    elif command_list[1] == "odd":
        for index, number in enumerate(num_list):
            if number >= max_even and number % 2 != 0:
                max_even = number
                max_index = index
                is_found = True
        if is_found:
            return max_index
        else:
            return "No matches"


def min_even_odd(num_list):
    min_index = 0
    min_even = 2 ** 31
    is_found = False
    if command_list[1] == "even":
        for index, number in enumerate(num_list):
            if number <= min_even and number % 2 == 0:
                min_even = number
                min_index = index
                is_found = True
        if is_found:
            return min_index
        else:
            return "No matches"
    elif command_list[1] == "odd":
        for index, number in enumerate(num_list):
            if number <= min_even and number % 2 != 0:
                min_even = number
                min_index = index
                is_found = True
        if is_found:
            return min_index
        else:
            return "No matches"


def first_last(count, num_list):
    if command_list[0] == "first":
        if count > len(num_list):
            return "Invalid count"
        else:
            if command_list[2] == "even" and len(even_list) > 0:
                return even_list[:count]
            elif command_list[2] == "odd" and len(odd_list) > 0:
                return odd_list[:count]
            else:
                return []
    elif command_list[0] == "last":
        if count > len(num_list):
            return "Invalid count"
        else:
            if command_list[2] == "even" and len(even_list) > 0:
                even_list.reverse()
                last_evens = list(even_list[:count])
                last_evens.reverse()
                return last_evens
            elif command_list[2] == "odd" and len(odd_list) > 0:
                odd_list.reverse()
                last_odds = odd_list[:count]
                last_odds.reverse()
                return last_odds
            else:
                return []


command = input()

while command != "end":
    command_list = command.split()
    even_list = [i for i in numbers_list if i % 2 == 0]
    odd_list = [i for i in numbers_list if i % 2 != 0]

    if command_list[0] == "exchange":
        exchanged_list = exchange(int(command_list[1]), numbers_list)
        numbers_list = exchanged_list
    elif command_list[0] == "max":
        print(max_even_odd(numbers_list))
    elif command_list[0] == "min":
        print(min_even_odd(numbers_list))
    elif command_list[0] == "first":
        print(first_last(int(command_list[1]), numbers_list))
    elif command_list[0] == "last":
        print(first_last(int(command_list[1]), numbers_list))
    command = input()
print(numbers_list)
