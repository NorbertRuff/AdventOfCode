from utils import read_file

"""
input:
10  13  16  21  30  45  = 68

step 1:
get inner numbers that increment
3   3   5   9  15 = 23
 
step 2
do the same for the inner numbers until you get all zeros
0   2   4   6 = 8

step 3
2   2   2 = 2

step 4
0 0 = 0

step 5
add the numbers from step 1 to step 4
0+2 
2+6
8+15
23+48
"""


def get_to_all_0(values):
    while True:
        next_values = [values[-1][i + 1] - values[-1][i] for i in range(len(values[-1]) - 1)]
        values.append(next_values)
        if all(number == 0 for number in next_values):
            break


def get_prediction(values):
    values[-1].append(0)
    values[-1].insert(0, 0)
    for i in range(len(values) - 2, -1, -1):
        values[i].append(values[i][-1] + values[i + 1][-1])
        values[i].insert(0, values[i][0] - values[i + 1][0])
    return values[0][-1]


def part1_resolver(histories):
    result = 0
    for history in histories:
        get_to_all_0(history)
        result += get_prediction(history)
    return result


def part2_resolver(histories):
    part2_result = 0
    for history in histories:
        get_to_all_0(history)
        get_prediction(history)
        part2_result += history[0][0]
    return part2_result


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    histories_list_of_lists = [x for x in raw_data]
    histories_list_of_lists = [[list(map(int, x.split()))] for x in histories_list_of_lists]
    first_part_result = part1_resolver(histories_list_of_lists)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(histories_list_of_lists)
    print('second_part_result', second_part_result)
