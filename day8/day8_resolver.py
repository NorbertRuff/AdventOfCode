from typing import List

from utils import *

raw_data = read_file("./day8/day8-input.txt")


def get_matrix_from_raw_data():
    grid = []
    for i, row in enumerate(raw_data.splitlines()):
        grid.append([])
        for tree in list(row.strip()):
            grid[i].append(tree)
    print(grid)
    return grid


matrix: List[List[int]] = get_matrix_from_raw_data()
length = len(matrix)
width = len(matrix[0])


def up(tree, x, y):
    for i in range(x - 1, 0, -1):
        if tree <= matrix[i][y]:
            return False
    return True


def down(tree, x, y):
    for i in range(x + 1, length):
        if tree <= matrix[i][y]:
            return False
    return True


def left(tree, x, y):
    for i in range(y - 1, 0, -1):
        if tree <= matrix[x][i]:
            return False
    return True


def right(tree, x, y):
    for i in range(y + 1, width):
        if tree <= matrix[x][i]:
            return False
    return True


def visible_from_outside(x, y):
    tree = matrix[x][y]
    if up(tree, x, y) or down(tree, x, y) or left(tree, x, y) or right(tree, x, y):
        return True
    return False


def get_day8_results():
    inner_count = 0
    for i in range(length):
        for j in range(width):
            if visible_from_outside(i, j):
                inner_count += 1
    print(inner_count)
    part1 = inner_count + (2 * length) + (2 * width) - 4
    print(part1)
    return part1
