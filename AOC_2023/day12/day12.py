from utils import read_file

arrangements = {}


def find_arrangement(dots, blocks, current_pos_dots, current_pos_blocks, number_of_hash):
    key = (current_pos_dots, current_pos_blocks, number_of_hash)
    if key in arrangements:
        return arrangements[key]
    if current_pos_dots == len(dots):
        if current_pos_blocks == len(blocks) and number_of_hash == 0:
            return 1
        elif current_pos_blocks == len(blocks) - 1 and blocks[current_pos_blocks] == number_of_hash:
            return 1
        else:
            return 0
    result = 0
    for character in ['.', '#']:
        if dots[current_pos_dots] == character or dots[current_pos_dots] == '?':
            if character == '.' and number_of_hash == 0:
                result += find_arrangement(dots, blocks, current_pos_dots + 1, current_pos_blocks, 0)
            elif character == '.' and number_of_hash > 0 and current_pos_blocks < len(blocks) and blocks[
                current_pos_blocks] == number_of_hash:
                result += find_arrangement(dots, blocks, current_pos_dots + 1, current_pos_blocks + 1, 0)
            elif character == '#':
                result += find_arrangement(dots, blocks, current_pos_dots + 1, current_pos_blocks, number_of_hash + 1)
    arrangements[key] = result
    return result


def part1_resolver(raw_data):
    result = 0
    for line in raw_data:
        dots, blocks = line.split()
        blocks = [int(x) for x in blocks.split(',')]
        arrangements.clear()
        score = find_arrangement(dots, blocks, 0, 0, 0)
        result += score
    return result


def part2_resolver(raw_data):
    result = 0
    for line in raw_data:
        dots, blocks = line.split()
        dots = '?'.join([dots, dots, dots, dots, dots])
        blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
        blocks = [int(x) for x in blocks.split(',')]
        arrangements.clear()
        score = find_arrangement(dots, blocks, 0, 0, 0)
        result += score
    return result


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
