from typing import List

from utils import *

raw_data = read_file_no_strip("./day11/day11-input.txt").split('\n\n')


class Monkey:
    items: List[int]
    operation: str
    div: int
    if_true: int
    if_false: int

    def __init__(self, data):
        self.inspections = 0
        lines = data.split('\n')
        str_items = lines[1].split(': ')[1].split(', ')
        self.items = [int(item) for item in str_items]
        self.operation = lines[2].split('= ')[1].split(' ')
        self.div = int(lines[3].split()[-1])
        self.if_true = int(lines[4].split()[-1])
        self.if_false = int(lines[5].split()[-1])

    def turn(self, monkeys, divided):
        for item in self.items:
            self.inspections += 1
            self.send_item_new_value_to_monkey(item, monkeys, divided)
        self.items.clear()

    def send_item_new_value_to_monkey(self, item, monkeys, divided):
        res = self.check_operation(item)
        res = res // 3 if divided else res
        if res % self.div == 0:
            # print(f"item {item} is divisible by {self.div}, returning {x} to {y}")
            monkeys[self.if_true].items.append(res)
        else:
            # print(f"item {item} is not divisible by {self.div}, returning {x} to {y}")
            monkeys[self.if_false].items.append(res)

    def check_operation(self, item):
        res = 0
        if self.operation[1] == '+':
            if self.operation[2] == 'old':
                res = item + item
            else:
                res = item + int(self.operation[2])
        elif self.operation[1] == '*':
            if self.operation[2] == 'old':
                res = item * item
            else:
                res = item * int(self.operation[2])
        return res


def get_day11_part1_results():
    monkeys = [Monkey(x) for x in raw_data]
    for iteration in range(20):
        for monkey in monkeys:
            monkey.turn(monkeys, True)
    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def get_day11_part2_results():
    monkeys = [Monkey(x) for x in raw_data]
    for iteration in range(10000):
        for monkey in monkeys:
            monkey.turn(monkeys, False)
    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]
