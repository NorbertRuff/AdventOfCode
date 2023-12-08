from utils import read_file


def part1_resolver(instructions, raw_network):
    refined_network = {}
    current_location = 'AAA'
    for item in raw_network:
        location, right_left = item.split(' = ')
        left, right = right_left.strip().split(',')
        refined_network[location] = (left[1:].strip(), right[:-1].strip())
    print(refined_network)
    counter = 0
    i = 0
    while current_location != 'ZZZ':
        if instructions[i] == 'R':
            print(current_location, '-> R ->', refined_network[current_location][1])
            counter += 1
            current_location = refined_network[current_location][1]
        if instructions[i] == 'L':
            print(current_location, '-> L ->', refined_network[current_location][0])
            counter += 1
            current_location = refined_network[current_location][0]
        if i == len(instructions) - 1:
            i = 0
        else:
            i += 1
    print(current_location, instructions[i], refined_network[current_location])
    return counter


def part2_resolver(instructions, raw_network):
    refined_network = {}

    for item in raw_network:
        location, right_left = item.split(' = ')
        left, right = right_left.strip().split(',')
        refined_network[location] = (left[1:].strip(), right[:-1].strip())

    current_locations = [value for value in refined_network.keys() if value[-1] == 'A']
    print(current_locations)

    counter = 0
    i = 0
    while True:
        if instructions[i] == 'R':
            counter += 1
            current_locations = [refined_network[current_location][1] for current_location in current_locations]
            print(current_locations)
        if instructions[i] == 'L':
            counter += 1
            current_locations = [refined_network[current_location][0] for current_location in current_locations]
            print(current_locations)
        if i == len(instructions) - 1:
            i = 0
        else:
            i += 1
        if all([current_location[-1] == 'Z' for current_location in current_locations]):
            break

    return counter


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    instructions = raw_data[0]
    instructions = [i for i in instructions if i != ' ']
    network = raw_data[2:]
    first_part_result = part1_resolver(instructions, network)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(instructions, network)
    print('second_part_result', second_part_result)
