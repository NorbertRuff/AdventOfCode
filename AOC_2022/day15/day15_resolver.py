import re

from utils import *

raw_data = read_file("./day15/day15-input.txt").splitlines()


def get_day15_results():
    sensors = set()
    beacons = set()
    sum_d = 0
    for line in raw_data:
        numbers = [int(x) for x in re.findall(r"-?\d+\.?\d*", line)]
        sens_x, sens_y, beacon_x, beacon_y = numbers[0], numbers[1], numbers[2], numbers[3]
        distance = abs(sens_x-beacon_x) + abs(sens_y-beacon_y)
        sum_d += distance
        sensors.add((sens_x, sens_y, distance))
        beacons.add((beacon_x, beacon_y))
    print(sensors)
    print(beacons)

    y = 2000000
    xx = set()

    def manhattan(sx, sy, bx, by):
        return abs(sx - bx) + abs(sy - by)

    for i in range(len(beacons)):

        x = manhattan(sx, sy, bx, by) - abs(sy - y)
        xx.update(range(sx - x, sx + x + 1))
        if by == y:
            xx.discard(bx)

    print(len(xx))


