from itertools import combinations

from utils import read_file


def get_columns(raw_data):
    cols = []
    for ii in range(len(raw_data[0])):
        for i in range(len(raw_data)):
            if raw_data[i][ii] == "#":
                break
        else:
            cols.append(ii)
    return cols


def get_stars(raw_data):
    stars = []
    for i, row in enumerate(raw_data):
        for ii, column in enumerate(row):
            if column == '#':
                stars.append((i, ii))
    return stars


def part1_resolver(raw_data):
    stars = get_stars(raw_data)
    cols = get_columns(raw_data)
    rows = [i for i, row in enumerate(raw_data) if '#' not in row]

    print(stars)
    print(cols)
    print(rows)

    result = 0
    for left, right in combinations(stars, 2):
        bl, sl = (left[0], right[0]) if left[0] > right[0] else (right[0], left[0])
        br, sr = (left[1], right[1]) if left[1] > right[1] else (right[1], left[1])
        diff = abs(right[0] - left[0]) + abs(right[1] - left[1])
        result += diff
        for row in rows:
            if sl < row < bl:
                result += 1
        for column in cols:
            if sr < column < br:
                result += 1

    return result


def part2_resolver(raw_data):
    stars = get_stars(raw_data)
    cols = get_columns(raw_data)
    rows = [i for i, row in enumerate(raw_data) if '#' not in row]

    print(stars)
    print(cols)
    print(rows)

    result = 0
    for left, right in combinations(stars, 2):
        bleft, sleft = (left[0], right[0]) if left[0] > right[0] else (right[0], left[0])
        bright, sright = (left[1], right[1]) if left[1] > right[1] else (right[1], left[1])
        diff = abs(right[0] - left[0]) + abs(right[1] - left[1])
        result += diff
        for row in rows:
            if sleft < row < bleft:
                result += 999999
        for column in cols:
            if sright < column < bright:
                result += 999999

    return result


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
