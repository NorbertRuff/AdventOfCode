from utils import *

intervals = [20, 60, 100, 140, 180, 220]
raw_data = read_file("./day10/day10-input.txt").splitlines()


def get_day10_part1_results():
    cycle = 0
    tick = 1
    strength = 0
    for line in raw_data:
        instruction, *value = line.split(" ")
        value = value[0] if value else None
        if instruction == "noop":
            cycle, strength = get_signal(cycle, tick, strength)
        if instruction == "addx":
            cycle, strength = get_signal(cycle, tick, strength)
            cycle, strength = get_signal(cycle, tick, strength)
            tick += int(value)
    return strength


def get_signal(cycle, register, signal_strength):
    cycle += 1
    if cycle in intervals:
        signal_strength += cycle * register
    return cycle, signal_strength


def get_day10_part2_results():
    tick = 1
    display = []
    row = ""
    for line in raw_data:
        instruction, *value = line.split(" ")
        value = value[0] if value else None
        for c in range(2):
            if len(row) in range(tick - 1, tick + 2):
                row += "X"
            else:
                row += "."
            if len(row) == 40:
                display.append(row)
                row = ""
            if instruction == "noop":
                break
        if instruction == "addx":
            tick += int(value)
    for line in display:
        print(line)
