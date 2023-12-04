from collections import defaultdict

from utils import read_file_no_strip

test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

"""
There are lots of numbers and symbols you don't really understand,
 but apparently any number adjacent to a symbol, even diagonally,
  is a "part number" and should be included in your sum.
"""

numbers = '0123456789'


def get_cell(data, x, y):
    try:
        return data[y][x]
    except IndexError:
        pass


def part1_resolver(data):
    number = ''
    include = False
    summa = 0
    gears = defaultdict(list)
    gear = None

    for i in range(len(data)):
        for j in range(len(data[i]) + 1):
            cell = get_cell(data, j, i)
            if cell and cell in numbers:
                number += cell
                for ii in (i - 1, i, i + 1):
                    for jj in (j - 1, j, j + 1):
                        cell2 = get_cell(data, jj, ii)
                        if cell2 and cell2 not in numbers and cell2 != '.':
                            include = True
                            if cell2 == '*':
                                gear = (jj, ii)
            else:
                if number:
                    if include:
                        summa += int(number)
                    if gear:
                        gears[gear].append(int(number))

                    number = ''
                    include = False
                    gear = None
    return gears, summa


def part2_resolver(gears):
    total = 0
    for gear, index in gears.items():
        if len(index) == 2:
            total += index[0] * index[1]
    return total


if __name__ == '__main__':
    puzzle_input = read_file_no_strip('./input.txt').splitlines()
    gears, first_part_result = part1_resolver(puzzle_input)
    print('first_part_result',
          first_part_result)
    second_part_result = part2_resolver(gears)
    print('second_part_result', second_part_result)
