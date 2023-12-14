from utils import read_file


def part1_resolver(raw_data):
    return 2


def part2_resolver(raw_data):
    return 2


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
