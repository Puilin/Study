import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, line.split())

    x_new, y_new = 0.000, 0.000
    if x2 == x3 and y2 == y3:
        x_new = (x1 + x4) - x2
        y_new = (y1 + y4) - y2
    if x2 == x4 and y2 == y4:
        x_new = (x1 + x3) - x2
        y_new = (y1 + y3) - y2
    if x1 == x3 and y1 == y3:
        x_new = (x2 + x4) - x1
        y_new = (y2 + y4) - y1
    if x1 == x4 and y1 == y4:
        x_new = (x2 + x3) - x1
        y_new = (y2 + y3) - y1

    print(f"{x_new:.3f} {y_new:.3f}")