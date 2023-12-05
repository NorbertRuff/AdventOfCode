import math
from utils import *

raw_data = read_file("./day12/day12-input.txt").splitlines()
grid = []
elevations = []


# https://en.wikipedia.org/wiki/Breadth-first_search
def breadth_first_search(end):
    end_dict = dict()
    queue = [end]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(queue) > 0:
        curr = queue.pop(0)
        for direction in directions:
            next_row = curr[0] + direction[0]
            next_col = curr[1] + direction[1]
            if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                continue
            if grid[curr[0]][curr[1]] <= grid[next_row][next_col] + 1 and (next_row, next_col) not in end_dict:
                end_dict[(next_row, next_col)] = curr[2] + 1
                queue.append((next_row, next_col, curr[2] + 1))
    return end_dict


def get_day12_results():
    start = ()
    end = ()
    for row, line in enumerate(raw_data):
        grid.append([])
        for col, elevation in enumerate(line):
            grid[row].append(elevation)
            if grid[row][col] == "a":
                elevations.append((row, col))
            if elevation == "S":
                start = (row, col, 1)
                grid[row][col] = 25
            elif elevation == "E":
                end = (row, col, 0)
                grid[row][col] = 25
            else:
                grid[row][col] = ord(grid[row][col]) - 97
    print(start, end)
    print(grid)
    end_dict = breadth_first_search(end)
    minimum = math.inf
    for i in elevations:
        try:
            if end_dict[i] < minimum:
                minimum = end_dict[i]
        except KeyError:
            continue
    print(minimum)
    return end_dict[(start[0], start[1])], minimum
