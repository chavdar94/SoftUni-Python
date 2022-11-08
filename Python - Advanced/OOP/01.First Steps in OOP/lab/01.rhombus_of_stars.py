size = int(input())


def draw_lines(n, row):
    spaces = n - row
    stars = n - spaces
    print(' ' * spaces + '* ' * stars)


def draw_upper(n):
    for row in range(1, n + 1):
        draw_lines(n, row)


def draw_bottom(n):
    for row in range(n - 1, -1, -1):
        draw_lines(n, row)


def draw_rhombus():
    draw_upper(size)
    draw_bottom(size)


draw_rhombus()
