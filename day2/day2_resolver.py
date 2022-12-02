from utils import read_file
from enum import Enum


# Enum class is now a thing. Syntax https://docs.python.org/3/library/enum.html
class RockPaperScissorsPlayer(Enum):
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"


class RockPaperScissorsEnemy(Enum):
    X = "ROCK"
    Y = "PAPER"
    Z = "SCISSORS"


def play_a_game(player, enemy):
    if player == RockPaperScissorsPlayer.A:
        if enemy == RockPaperScissorsEnemy.X:
            return 4
        if enemy == RockPaperScissorsEnemy.Y:
            return 8
        elif enemy == RockPaperScissorsEnemy.Z:
            return 3
    elif player == RockPaperScissorsPlayer.B:
        if enemy == RockPaperScissorsEnemy.X:
            return 1
        if enemy == RockPaperScissorsEnemy.Y:
            return 5
        elif enemy == RockPaperScissorsEnemy.Z:
            return 9
    elif player == RockPaperScissorsPlayer.C:
        if enemy == RockPaperScissorsEnemy.X:
            return 7
        if enemy == RockPaperScissorsEnemy.Y:
            return 2
        elif enemy == RockPaperScissorsEnemy.Z:
            return 6


def get_day2_results_for_first_part():
    raw_data = read_file("./day2/day2-input.txt").splitlines()
    result = 0
    for line in raw_data:
        x, y = line.split(" ") # tuple unpacking
        result += play_a_game(RockPaperScissorsPlayer[x], RockPaperScissorsEnemy[y])
    print(result)


def play_a_game_part2(player, enemy):
    if player == RockPaperScissorsPlayer.A:
        if enemy == RockPaperScissorsEnemy.X:
            return 3
        if enemy == RockPaperScissorsEnemy.Y:
            return 4
        elif enemy == RockPaperScissorsEnemy.Z:
            return 8
    elif player == RockPaperScissorsPlayer.B:
        if enemy == RockPaperScissorsEnemy.X:
            return 1
        if enemy == RockPaperScissorsEnemy.Y:
            return 5
        elif enemy == RockPaperScissorsEnemy.Z:
            return 9
    elif player == RockPaperScissorsPlayer.C:
        if enemy == RockPaperScissorsEnemy.X:
            return 2
        if enemy == RockPaperScissorsEnemy.Y:
            return 6
        elif enemy == RockPaperScissorsEnemy.Z:
            return 7


def get_day2_results_for_second_part():
    raw_data = read_file("./day2/day2-input.txt").splitlines()
    result = 0
    for line in raw_data:
        x, y = line.split(" ") # tuple unpacking
        result += play_a_game_part2(RockPaperScissorsPlayer[x], RockPaperScissorsEnemy[y])
    print(result)
