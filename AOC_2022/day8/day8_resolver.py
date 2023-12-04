from typing import List

from utils import *

raw_data = read_file("./day8/day8-input.txt")


def get_matrix_from_raw_data():
    grid = []
    for i, row in enumerate(raw_data.splitlines()):
        grid.append([])
        for tree in list(row.strip()):
            grid[i].append(tree)
    return grid


matrix: List[List[int]] = get_matrix_from_raw_data()
length = len(matrix)
width = len(matrix[0])


def up(trees, x, y):
    for i in range(1, x + 1):
        if trees[x][y] <= trees[x - i][y]:
            return False
        if x - i == 0:
            return True


def down(trees, x, y):
    for i in range(x + 1, length):
        if trees[i][y] >= trees[x][y]:
            return False
        if i == length - 1:
            return True


def left(trees, x, y):
    for i in range(1, y + 1):
        if trees[x][y] <= trees[x][y - i]:
            return False
        if y - i == 0:
            return True


def right(trees, x, y):
    for i in range(y + 1, width):
        if trees[x][i] >= trees[x][y]:
            return False
        if i == width - 1:
            return True


def up_score(trees, x, y):
    up_s = 0
    for i in range(y - 1, -1, -1):
        if trees[x][y] <= trees[x][i]:
            up_s += 1
            break
        up_s += 1
    return up_s


def down_score(trees, x, y):
    down_s = 0
    for i in range(y + 1, len(trees[x])):
        if trees[x][y] <= trees[x][i]:
            down_s += 1
            break
        down_s += 1
    return down_s


def left_score(trees, x, y):
    left_s = 0
    for i in range(x - 1, -1, -1):
        if trees[x][y] <= trees[i][y]:
            left_s += 1
            break
        left_s += 1
    return left_s


def right_score(trees, x, y):
    right_s = 0
    for i in range(x + 1, len(trees)):
        if trees[x][y] <= trees[i][y]:
            right_s += 1
            break
        right_s += 1
    return right_s


def visible_from_outside(trees, x, y):
    if x == 0 or y == 0 or x == length - 1 or y == width - 1:
        return True
    if up(trees, x, y) or down(trees, x, y) or left(trees, x, y) or right(trees, x, y):
        return True
    return False


def get_scenic_score(trees, x, y):
    left_total = left_score(trees, x, y)
    top_total = up_score(trees, x, y)
    right_total = right_score(trees, x, y)
    bottom_total = down_score(trees, x, y)
    return left_total * top_total * bottom_total * right_total


def get_day8_part1_results():
    total = 0
    for i in range(length):
        for j in range(width):
            if visible_from_outside(matrix, i, j):
                total += 1
    return total


def get_day8_part2_results():
    total = 0
    for i in range(length):
        for j in range(width):
            x = get_scenic_score(matrix, i, j)
            if x > total:
                total = x
    return total
