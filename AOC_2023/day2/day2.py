import re

from utils import read_file_strip, read_file_no_strip

total_cubes = {'red': 12, 'green': 13, 'blue': 14}


def is_valid_hand(cubes):
    for cube in cubes:
        amount, color = cube.split()
        if int(amount) > total_cubes[color]:
            return False
    return True


def is_valid_game(hands):
    for hand in hands:
        cubes = hand.split(',')
        if not is_valid_hand(cubes):
            return False
    return True


def part1_resolver():
    p1_input = read_file_strip('input1.txt').split('\n')
    invalid_games = []
    for game in p1_input:
        [game_number, hands] = game.split(':')
        game_number = re.findall(r'\d+', game_number)[0]
        hands = [hand.strip() for hand in hands.split(';')]
        print(game_number, hands)
        if is_valid_game(hands):
            invalid_games.append(game_number)
    return sum(int(game_number) for game_number in invalid_games)


def find_smallest_cubes(hand):
    cubes = hand.split(',')
    smallest_red_in_hand = 12
    smallest_green_in_hand = 13
    smallest_blue_in_hand = 14
    for cube in cubes:
        amount, color = cube.split()
        if color == 'red' and int(amount) < smallest_red_in_hand:
            smallest_red_in_hand = int(amount)
        elif color == 'green' and int(amount) < smallest_green_in_hand:
            smallest_green_in_hand = int(amount)
        elif color == 'blue' and int(amount) < smallest_blue_in_hand:
            smallest_blue_in_hand = int(amount)
    return smallest_red_in_hand, smallest_green_in_hand, smallest_blue_in_hand


def part2_resolver():
    p2_input = read_file_strip('input1.txt').splitlines()
    games_list = []
    for game in p2_input:
        game_number, hands = game.split(':')
        game_number = re.findall(r'\d+', game_number)[0]
        hands = [hand.strip() for hand in hands.split(';')]
        game_dict = {int(game_number): []}
        for hand in hands:
            smallest_red_in_hand, smallest_green_in_hand, smallest_blue_in_hand = find_smallest_cubes(hand)
            game_dict[int(game_number)].append(
                {'red': smallest_red_in_hand, 'green': smallest_green_in_hand, 'blue': smallest_blue_in_hand})
        games_list.append(game_dict)
        print(games_list)
    return games_list


if __name__ == '__main__':
    # first_part_result = part1_resolver()
    # print('first_part_result', first_part_result)
    second_part_result = part2_resolver()
    print('second_part_result', second_part_result)
