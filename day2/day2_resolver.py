from utils import read_file
from enum import Enum


# Enum class is now a thing in python. Syntax https://docs.python.org/3/library/enum.html
class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# So I used it
class Symbols(Enum):
    A = X = RockPaperScissors.ROCK
    B = Y = RockPaperScissors.PAPER
    C = Z = RockPaperScissors.SCISSORS


# a lot
class Score(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


def play_a_game_part_1(player: RockPaperScissors, enemy: RockPaperScissors) -> int:
    if player == RockPaperScissors.ROCK:
        if enemy == RockPaperScissors.ROCK:
            return Score.DRAW.value
        elif enemy == RockPaperScissors.PAPER:
            return Score.LOSE.value
        elif enemy == RockPaperScissors.SCISSORS:
            return Score.WIN.value
    elif player == RockPaperScissors.PAPER:
        if enemy == RockPaperScissors.PAPER:
            return Score.DRAW.value
        elif enemy == RockPaperScissors.ROCK:
            return Score.WIN.value
        elif enemy == RockPaperScissors.SCISSORS:
            return Score.LOSE.value
    elif player == RockPaperScissors.SCISSORS:
        if enemy == RockPaperScissors.SCISSORS:
            return Score.DRAW.value
        elif enemy == RockPaperScissors.ROCK:
            return Score.LOSE.value
        elif enemy == RockPaperScissors.PAPER:
            return Score.WIN.value


def play_a_game_part_2(enemy: RockPaperScissors):
    if enemy == RockPaperScissors.ROCK:
        return Score.DRAW.value
    elif enemy == RockPaperScissors.PAPER:
        return Score.LOSE.value
    elif enemy == RockPaperScissors.SCISSORS:
        return Score.WIN.value


def get_day2_results_for_first_part() -> int:
    raw_data = read_file("./day2/day2-input.txt").splitlines()
    result = 0
    for line in raw_data:
        x, y = line.split(" ")  # tuple unpacking
        result += Symbols[y].value.value
        result += play_a_game_part_1(Symbols[y].value, Symbols[x].value)
    return result


def get_day2_results_for_second_part() -> int:
    raw_data = read_file("./day2/day2-input.txt").splitlines()
    result = 0
    for line in raw_data:
        x, y = line.split(" ")  # tuple unpacking
        result += Symbols[y].value.value
        result += play_a_game_part_2(Symbols[x].value)
    return result
