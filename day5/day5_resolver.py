from copy import deepcopy
from utils import read_file

part_1_crates = {
    1: ['L', 'C', 'G', 'M', 'Q'],
    2: ['G', 'H', 'F', 'T', 'C', 'L', 'D', 'R'],
    3: ['R', 'W', 'T', 'M', 'N', 'F', 'J', 'V'],
    4: ['P', 'Q', 'V', 'D', 'F', 'J'],
    5: ['T', 'B', 'L', 'S', 'M', 'F', 'N'],
    6: ['P', 'D', 'C', 'H', 'V', 'N', 'R'],
    7: ['T', 'C', 'H'],
    8: ['P', 'H', 'N', 'Z', 'V', 'J', 'S', 'G'],
    9: ['G', 'H', 'F', 'Z']
}

part1_test_crates = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}

part_2_crates = deepcopy(part_1_crates)
part2_test_crates = deepcopy(part1_test_crates)


def get_instructions():
    raw_data = read_file("./day5/day5-instructions-input.txt")
    instructions = []
    for instruction in raw_data.splitlines():
        instructions.append([int(s) for s in instruction.split() if s.isdigit()])
    return instructions


def move_boxes_part1(q, s, d):
    for _ in range(q):
        print("moving box from {} to {}".format(s, d))
        part1_test_crates[d].append(part1_test_crates[s][-1])
        part1_test_crates[s].pop()


def move_boxes_part2(q, s, d):
    part2_test_crates[d].extend([part2_test_crates[s].pop() for _ in range(q)][::-1])


def get_day5_results_for_first_part():
    instructions = get_instructions()
    for quantity, source, destination in instructions:
        move_boxes_part1(quantity, source, destination)
    result = ""
    for i in part1_test_crates:
        result += part1_test_crates[i][-1]
    return result


def get_day5_results_for_second_part():
    instructions = get_instructions()
    for quantity, source, destination in instructions:
        move_boxes_part2(quantity, source, destination)
    result = ""
    for i in part1_test_crates:
        result += part1_test_crates[i][-1]
    return result
