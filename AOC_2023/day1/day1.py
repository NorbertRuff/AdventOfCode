import re

mapper = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_input(filename):
    if not filename:
        AssertionError("Filename is empty")
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def get_first_isdigit_in_string(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]


def day1_part1_resolver():
    lines = read_input('./input1.txt')
    summa = 0
    for line in lines:
        first_isdigit = get_first_isdigit_in_string(line)
        last_isdigit = get_first_isdigit_in_string(line[::-1])
        summa += int(first_isdigit + last_isdigit)
    return summa


def day1_part2_resolver():
    lines = read_input('./input2.txt')
    result = 0
    for line in lines:
        regex = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
        regex_finds = regex.findall(line)

        for i in range(len(regex_finds)):
            if len(regex_finds[i]) > 1:
                regex_finds[i] = mapper[regex_finds[i]]
        result += int(regex_finds[0] + regex_finds[-1])
    return result


if __name__ == '__main__':
    first_part_result = day1_part1_resolver()
    print('first_part_result', first_part_result)
    second_part_result = day1_part2_resolver()
    print('second_part_result', second_part_result)
