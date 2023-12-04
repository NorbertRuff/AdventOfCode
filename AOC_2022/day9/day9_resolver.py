from enum import Enum
from utils import *


class Directions(Enum):
    U = (0, 1)
    D = (0, -1)
    L = (-1, 0)
    R = (1, 0)


def tail_move(tail, head):
    if not (abs(tail[1] - head[1]) > 1 or abs(tail[0] - head[0]) > 1):
        return tail
    if head[0] > tail[0]:
        tail = (Directions.R.value[0] + tail[0], tail[1])
    elif head[0] < tail[0]:
        tail = (Directions.L.value[0] + tail[0], tail[1])
    if head[1] > tail[1]:
        tail = (tail[0], Directions.U.value[1] + tail[1])
    elif head[1] < tail[1]:
        tail = (tail[0], Directions.D.value[1] + tail[1])
    return tail


def simulate(tail_length):
    raw_data = read_file("./day9/day9-input.txt").splitlines()
    route = {(0, 0)}
    head = (0, 0)
    tail = [head] * tail_length
    for line in raw_data:
        direction, count = line.split(" ")
        for _ in range(int(count)):
            x, y = Directions[direction].value
            head = (head[0] + x, head[1] + y)
            temp = head
            for i, j in enumerate(tail, 0):
                tail[i] = tail_move(j, temp)
                temp = tail[i]
            route.add(tail[-1])
    return len(route)


def get_day9_part1_results():
    return simulate(1)


def get_day9_part2_results():
    return simulate(9)
