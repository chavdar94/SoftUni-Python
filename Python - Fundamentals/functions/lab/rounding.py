numbers = input().split()


def rounded(nums):
    numbers_list = [float(num) for num in numbers]
    # for num in range(len(numbers_list)):
    #     numbers_list[num] = round(numbers_list[num])
    numbers_list = [round(num) for num in numbers_list]
    return numbers_list


print(rounded(numbers))
