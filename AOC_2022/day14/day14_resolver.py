from utils import *

raw_data = read_file("./day14/day14-input.txt")


def get_day14_results():
    floor = 0
    grid = {}
    rocks = []
    start = None
    for line in raw_data.split("\n"):
        for i, point in enumerate(line.split('->')):
            x, y = point.split(',')
            if i == 0:
                start = (int(x), int(y))
            else:
                rocks.append((int(x), int(y)))
    x, y = start
    grid[x, y] = "X"
    for new_x, new_y in rocks:
        while x != new_x or y != new_y:
            if new_x > x:
                x += 1
            elif new_x < x:
                x -= 1
            if new_y > y:
                y += 1
            elif new_y < y:
                y -= 1
            grid[x, y] = "X"
            floor = max(floor, y)
    floor += 2
    for x in range(-1000, 1000):
        grid[x, floor] = "X"
    while True:
        start_x, start_y = 500, 0
        if grid.get((start_x, start_y)) == "0":
            break
        while True:
            if grid.get((start_x, start_y + 1), None) is None:
                start_y = start_y + 1
            elif grid.get((start_x - 1, start_y + 1), None) is None:
                start_x = start_x - 1
                start_y = start_y + 1
            elif grid.get((start_x + 1, start_y + 1), None) is None:
                start_x = start_x + 1
                start_y = start_y + 1
            else:
                grid[start_x, start_y] = "0"
                break

    return (sum(1 for _, value in grid.items() if value == "0") - 1)
