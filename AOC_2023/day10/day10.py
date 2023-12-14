from utils import read_file

"""
    - "|" :is a vertical pipe connecting north and south.
    - "-" :is a horizontal pipe connecting east and west.
    - "L" :is a 90-degree bend connecting north and east.
    - "J" :is a 90-degree bend connecting north and west.
    - "7" :is a 90-degree bend connecting south and west.
    - "F" :is a 90-degree bend connecting south and east.
    - "." :is ground; there is no pipe in this tile.
    - "S" :is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

Pipes = ['|', '-', 'L', 'J', '7', 'F', '.', 'S']

valid_left_neighbours = {
    '|': ['|', 'J', '7', 'S', '.'],
    '-': ['-', 'L', 'F', 'S', '.'],
    'L': ['S', '.'],
    'J': ['-', 'S', '.'],
    '7': ['-', 'L', 'S', '.'],
    'F': ['-', 'L', 'S', '.'],
    '.': ['|', '-', 'L', 'J', '7', 'F', '.', 'S'],
    'S': ['|', '-', 'L', 'J', '7', 'F', '.', 'S']
}

valid_right_neighbours = {
    '|': ['|', 'L', 'F', 'S', '.'],
    '-': ['-', 'J', '7', 'S', '.'],
    'L': ['-', 'S', '.'],
    'J': ['|', 'S', '.'],
    '7': ['|', 'F', 'S', '.'],
    'F': ['|', 'J', 'S', '.'],
    '.': ['|', '-', 'L', 'J', '7', 'F', '.', 'S'],
    'S': ['|', '-', 'L', 'J', '7', 'F', '.', 'S']
}

valid_up_neighbours = {
    '|': ['|', 'F', '7', 'S', '.'],
    '-': ['-', 'J', 'L', 'S', '.'],
    'L': ['|', 'S', '.'],
    'J': ['|', 'S', '.'],
    '7': ['-', 'S', '.'],
    'F': ['-', 'S', '.'],
    '.': ['|', '-', 'L', 'J', '7', 'F', '.', 'S'],
    'S': ['|', '-', 'L', 'J', '7', 'F', '.', 'S']
}

valid_down_neighbours = {
    '|': ['|', 'J', 'L', 'S', '.'],
    '-': ['-', 'F', '7', 'S', '.'],
    'L': ['-', 'S', '.'],
    'J': ['-', 'S', '.'],
    '7': ['|', 'S', '.'],
    'F': ['|', 'S', '.'],
    '.': ['|', '-', 'L', 'J', '7', 'F', '.', 'S'],
    'S': ['|', '-', 'L', 'J', '7', 'F', '.', 'S']
}


def find_start_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == Pipes.START.value:
                return i, j


def check_where_to_go_from_start(grid, current_position):
    """check where to go from start position"""
    grid_height = len(grid)
    grid_width = len(grid[0])
    i, j = current_position
    if i == 0:
        # check down
        if grid[i + 1][j] != '.':
            return i + 1, j
    elif i == grid_height - 1:
        # check up
        if grid[i - 1][j] != '.':
            return i - 1, j
    elif j == 0:
        # check right
        if grid[i][j + 1] != '.':
            return i, j + 1
    elif j == grid_width - 1:
        # check left
        if grid[i][j - 1] != '.':
            return i, j - 1
    else:
        # check up, down, left, right
        if grid[i - 1][j] != '.':
            return i - 1, j
        elif grid[i + 1][j] != '.':
            return i + 1, j
        elif grid[i][j - 1] != '.':
            return i, j - 1
        elif grid[i][j + 1] != '.':
            return i, j + 1
    return None


def check_neighbour_for_start(grid, current_position):
    """check neighbour for start"""
    grid_height = len(grid)
    grid_width = len(grid[0])
    i, j = current_position
    if i == 0:
        # check down
        if grid[i + 1][j] == 'S':
            return True
    elif i == grid_height - 1:
        # check up
        if grid[i - 1][j] == 'S':
            return True
    elif j == 0:
        # check right
        if grid[i][j + 1] == 'S':
            return True
    elif j == grid_width - 1:
        # check left
        if grid[i][j - 1] == 'S':
            return True
    else:
        # check up, down, left, right
        if grid[i - 1][j] == 'S':
            return True
        elif grid[i + 1][j] == 'S':
            return True
        elif grid[i][j - 1] == 'S':
            return True
        elif grid[i][j + 1] == 'S':
            return True
    return False


def check_neighbour_for_next_step(grid, current_position):
    """check neighbour for next step"""
    i, j = current_position
    current_pipe = grid[i][j]
    if current_pipe == Pipes.VERTICAL.value:
        # check up, down
        if grid[i - 1][j] != '.':
            return i - 1, j
        elif grid[i + 1][j] != '.':
            return i + 1, j
    elif current_pipe == Pipes.HORIZONTAL.value:
        # check left, right
        if grid[i][j - 1] != '.':
            return i, j - 1
        elif grid[i][j + 1] != '.':
            return i, j + 1
    elif current_pipe == Pipes.NORTH_EAST.value:
        # check up, right
        if grid[i - 1][j] != '.':
            return i - 1, j
        elif grid[i][j + 1] != '.':
            return i, j + 1
    elif current_pipe == Pipes.NORTH_WEST.value:
        # check up, left
        if grid[i - 1][j] != '.':
            return i - 1, j
        elif grid[i][j - 1] != '.':
            return i, j - 1
    elif current_pipe == Pipes.SOUTH_WEST.value:
        # check down, left
        if grid[i + 1][j] != '.':
            return i + 1, j
        elif grid[i][j - 1] != '.':
            return i, j - 1
    elif current_pipe == Pipes.SOUTH_EAST.value:
        # check down, right
        if grid[i + 1][j] != '.':
            return i + 1, j
        elif grid[i][j + 1] != '.':
            return i, j + 1
    elif current_pipe == 0:
        # check up, down, left, right
        if grid[i - 1][j] != '.':
            return i - 1, j
        elif grid[i + 1][j] != '.':
            return i + 1, j
        elif grid[i][j - 1] != '.':
            return i, j - 1
        elif grid[i][j + 1] != '.':
            return i, j + 1
    print('Something wrong')
    return None


def part1_resolver(grid):
    start_position = find_start_position(grid)
    current_position = start_position
    distance = 0
    check_where_to_start = check_where_to_go_from_start(grid, current_position)
    if check_where_to_start:
        grid[current_position[0]][current_position[1]] = distance
        current_position = check_where_to_start
    print(check_where_to_start)
    print('< -------Start-------- >', start_position, '->', check_where_to_start)
    is_next_step_start = False
    while True:
        print('< ------------------ >')
        for line in grid:
            print(line)
        is_next_step_start = check_neighbour_for_start(grid, current_position)
        if is_next_step_start:
            print('Finish', is_next_step_start)
            break
        current_position = check_neighbour_for_next_step(grid, current_position)
        grid[current_position[0]][current_position[1]] = distance
        distance += 1
        continue
    return distance


def part2_resolver(raw_data):
    return 1


def get_map(raw_data):
    grid = []
    for line in raw_data:
        grid.append(list(line))
    return grid


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    # make a map(array of array) from raw_data
    grid = get_map(raw_data)
    for line in grid:
        print(line)
    first_part_result = part1_resolver(grid)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
