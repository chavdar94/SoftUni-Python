def even_numbers(nums):
    even_list = list(map(int, nums))
    even_list = list(filter(lambda x: x % 2 == 0, even_list))
    return even_list


numbers = input().split()
print(even_numbers(numbers))
