import re

from utils import read_file_no_strip


def get_start_index(regex, data):
    return [i for i, line in enumerate(data) if regex.search(line)][0]


def make_list_of_start_and_end_index(start_number, end_number):
    return [i for i in range(start_number, start_number + end_number)]


def split_data_to_groups(raw_data):
    raw_data = [line.split(' ') for line in raw_data]
    raw_data = [[int(num) for num in line] for line in raw_data]
    raw_data_dict = {}
    for i in range(len(raw_data)):
        for j in range(raw_data[i][2]):
            raw_data_dict[raw_data[i][1] + j] = raw_data[i][0] + j
    return raw_data_dict


def get_seeds(raw_data):
    seeds_regex = re.compile(r'seeds:')
    seeds = [line for line in raw_data if seeds_regex.search(line)][0]
    seeds = seeds.split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    return seeds


def get_line_dict(numbers):
    raw_dict = {}
    for i in range(numbers[2]):
        raw_dict[numbers[1] + i] = numbers[0] + i
    return raw_dict


def get_dicts(raw_data):
    maps = []
    map_dict = {}
    for line in raw_data[1:]:
        if not line:
            continue
        if 'map' in line:
            if map_dict:
                maps.append(map_dict)
                map_dict = {}
        else:
            numbers = [int(num) for num in line.split(' ')]
            map_dict.update(get_line_dict(numbers))
    maps.append(map_dict)
    return maps


def part1_resolver(raw_data):
    seeds = get_seeds(raw_data)
    dicts = get_dicts(raw_data)

    locations = []
    for seed in seeds:
        for i in range(len(dicts)):
            if seed in dicts[i]:
                seed = dicts[i][seed]
        locations.append(seed)
    return min(locations)


def part2_resolver(raw_data):
    seeds = get_seeds(raw_data)
    dicts = get_dicts(raw_data)
    new_seeds = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            new_seeds.extend(make_list_of_start_and_end_index(seeds[i], seeds[i + 1]))
        else:
            continue

    locations = []
    for seed in new_seeds:
        for i in range(len(dicts)):
            if seed in dicts[i]:
                seed = dicts[i][seed]
        locations.append(seed)

    return min(locations)


if __name__ == '__main__':
    raw_data = read_file_no_strip('./input2.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
