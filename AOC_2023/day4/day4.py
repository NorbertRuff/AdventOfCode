from utils import read_file_no_strip

test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

test_output = 13


def get_points(winning_numbers, my_numbers):
    points = 0
    for number in my_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points += points
            print(f"found number in winning numbers: {number} -> total: {points}")
    print('-------------------')
    return points


def get_points_for_part2(winning_numbers, my_numbers):
    points = 0
    for number in my_numbers:
        if number in winning_numbers:
            points += 1
    return points


def part1_resolver(data):
    summary = 0
    for index, line in enumerate(data):
        winning_numbers = line.split('|')[0].strip().split(':')[1].strip().split(' ')
        my_numbers = line.split('|')[1].strip().split(' ')
        winning_numbers = [int(x) for x in winning_numbers if x != '']
        my_numbers = [int(x) for x in my_numbers if x != '']
        print('-------------------')
        print(line)
        print(winning_numbers)
        print(my_numbers)
        points = get_points(winning_numbers, my_numbers)
        print('Points:', points)
        summary += points

    return summary


def part2_resolver(data):
    scratch_cards = {i: 1 for i in range(len(data))}
    for index, line in enumerate(data):
        winning_numbers = line.split('|')[0].strip().split(':')[1].strip().split(' ')
        my_numbers = line.split('|')[1].strip().split(' ')
        winning_numbers = [int(x) for x in winning_numbers if x != '']
        my_numbers = [int(x) for x in my_numbers if x != '']
        points = get_points_for_part2(winning_numbers, my_numbers)
        print(scratch_cards)
        for i in range(points):
            scratch_cards[index + i + 1] += scratch_cards[index]
    return sum(x for x in scratch_cards.values())


if __name__ == '__main__':
    puzzle_input = read_file_no_strip('./input.txt').splitlines()
    first_part_result = part1_resolver(puzzle_input)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(puzzle_input)
    print('second_part_result', second_part_result)
