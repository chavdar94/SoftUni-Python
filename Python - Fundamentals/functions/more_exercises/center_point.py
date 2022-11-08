from math import floor


def closest_point(x1, y1, x2, y2):
    x1y1 = abs(x1) + abs(y1)
    x2y2 = abs(x2) + abs(y2)

    if x1y1 <= x2y2:
        return f"{floor(x1), floor(y1)}"
    else:
        return f"{floor(x2), floor(y2)}"


x1_axis = float(input())
y1_axis = float(input())
x2_axis = float(input())
y2_axis = float(input())
print(closest_point(x1_axis, y1_axis, x2_axis, y2_axis))
