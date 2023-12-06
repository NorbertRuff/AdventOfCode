from utils import read_file

boat_speed = 1  # mm/s


def get_times(raw_data):
    times = raw_data[0].split(':')[1]
    times = times.split(' ')
    times = [int(time) for time in times if time != '']
    return times


def get_distances(raw_data):
    distances = raw_data[1].split(':')[1]
    distances = distances.split(' ')
    distances = [int(distance) for distance in distances if distance != '']
    return distances


def get_valid_times(time, distance):
    valid_times = []
    for i in range(time - 1):  # i = 3
        time_button_holded = i  # 3
        travel_time = time - i  # 7 - 3 = 4
        total_distance = time_button_holded * travel_time * boat_speed  # 3 * 4 * 1 = 12
        if total_distance > distance:
            valid_times.append(time_button_holded)
    return valid_times


def get_different_ways_to_win(times_distance_dict):
    ways_to_win = []
    for time, distance in times_distance_dict.items():
        times = get_valid_times(time, distance)
        ways_to_win.append(times)
    ways_to_win = [len(way) for way in ways_to_win]

    result = 1
    for way in ways_to_win:
        result *= way
    return result


def part1_resolver(raw_data):
    times = get_times(raw_data)
    distances = get_distances(raw_data)
    times_distance_dict = {}
    for i in range(len(times)):
        times_distance_dict[times[i]] = distances[i]
    ways_to_win = get_different_ways_to_win(times_distance_dict)
    return ways_to_win


def get_time_p2(raw_data):
    times = get_times(raw_data)
    total_time = ''
    for time in times:
        total_time += str(time)
    return int(total_time)


def get_distance_p2(raw_data):
    times = get_distances(raw_data)
    total_distance = ''
    for time in times:
        total_distance += str(time)
    return int(total_distance)


def part2_resolver(raw_data):
    time = get_time_p2(raw_data)
    distance = get_distance_p2(raw_data)
    print(time, distance)
    valid_times = get_valid_times(time, distance)
    return len(valid_times)


if __name__ == '__main__':
    raw_data = read_file('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
