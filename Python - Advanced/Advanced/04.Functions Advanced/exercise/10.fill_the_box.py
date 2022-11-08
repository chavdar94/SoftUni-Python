def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    cubes = args[3:]

    size = height * length * width

    for num in cubes:
        if num == 'Finish':
            break
        size -= int(num)

    if size >= 0:
        return f'There is free space in the box. You could put {size} more cubes.'
    else:
        return f'No more free space! You have {abs(size)} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
