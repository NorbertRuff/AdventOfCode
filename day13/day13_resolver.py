from utils import *

raw_data = read_file("./day13/day13-input.txt").split("\n\n")


def is_lower(pair_one, pair_two):
    if isinstance(pair_one, int) and isinstance(pair_two, int):
        if pair_one == pair_two:
            return None
        if pair_one < pair_two:
            return 1
        else:
            return -1
    if isinstance(pair_one, int):
        pair_one = [pair_one]
    if isinstance(pair_two, int):
        pair_two = [pair_two]
    for left, right in zip(pair_one, pair_two):
        rec = is_lower(left, right)
        if rec is not None:
            return rec
    if len(pair_one) < len(pair_two):
        return 1
    if len(pair_one) > len(pair_two):
        return -1
    return None


def get_day13_part1_results():
    result = []
    index_summa = 0
    for pairs in raw_data:
        if pairs:
            pair1, pair2 = pairs.split("\n")
            pair1 = eval(pair1)
            pair2 = eval(pair2)
            result.append(is_lower(pair1, pair2))
    for index, value in enumerate(result, start=1):
        if value == 1:
            index_summa += index
    return index_summa


def get_day13_part2_results():
    packets = []
    for pairs in raw_data:
        pair1, pair2 = pairs.split("\n")
        packets.append(eval(pair1))
        packets.append(eval(pair2))
    packets.append([[2]])
    packets.append([[6]])
    for i in range(len(packets)):
        for j in range(i, len(packets)):
            if is_lower(packets[i], packets[j]) == 1:
                packets[i], packets[j] = packets[j], packets[i]

    return packets.index([[2]]) * packets.index([[6]])
