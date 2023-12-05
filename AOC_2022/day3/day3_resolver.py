from utils import read_file


LOWERCASE_SHIFT = 96
UPPERCASE_SHIFT = 38


def get_day3_results_for_first_part():
    raw_data = read_file("./day3/day3-input.txt").splitlines()
    low_priority = []
    high_priority = []
    for line in raw_data:
        rucksack1_items = set(line[:len(line) // 2])
        rucksack2_items = set(line[len(line) // 2:])
        for item in rucksack1_items:
            if item in rucksack2_items:
                if item.islower():
                    low_priority.append(item)
                elif item.isupper():
                    high_priority.append(item)

    ascii_low_priority = [ord(item)-LOWERCASE_SHIFT for item in low_priority]
    ascii_high_priority = [ord(item)-UPPERCASE_SHIFT for item in high_priority]
    return sum(ascii_low_priority)+sum(ascii_high_priority)


def get_day3_results_for_second_part():
    raw_data = read_file("./day3/day3-input.txt").splitlines()
    result = 0
    try:
        for i in range(0, len(raw_data), 3):
            first_rucksack = set(raw_data[i])
            second_rucksack = set(raw_data[i+1])
            third_rucksack = set(raw_data[i+2])
            common_chars = third_rucksack.intersection(first_rucksack.intersection(second_rucksack))
            for item in common_chars:
                if item.islower():
                    result += ord(item) - LOWERCASE_SHIFT
                elif item.isupper():
                    result += ord(item) - UPPERCASE_SHIFT
    except IndexError:
        pass
    return result

