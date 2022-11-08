from math import floor


def longer_line(a1, b1, a2, b2, a3, b3, a4, b4):
    x1y1 = abs(a1) + abs(b1)
    x2y2 = abs(a2) + abs(b2)
    x3y3 = abs(a3) + abs(b3)
    x4y4 = abs(a4) + abs(b4)

    first_pair = x1y1 + x2y2
    second_pair = x3y3 + x4y4

    if first_pair >= second_pair:
        if x1y1 <= x2y2:
            print(f"{(floor(x1), floor(y1))}{(floor(x2), floor(y2))}")
        else:
            print(f"{(floor(x2), floor(y2))}{(floor(x1), floor(y1))}")
    else:
        if x3y3 <= x4y4:
            print(f"{(floor(x3), floor(y3))}{(floor(x4), floor(y4))}")
        else:
            print(f"{(floor(x4), floor(y4))}{(floor(x3), floor(y3))}")


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
