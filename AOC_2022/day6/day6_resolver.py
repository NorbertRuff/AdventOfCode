from utils import read_file


def get_day6_results_for_first_part():
    # input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    # input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    # input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    # input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    raw_data = read_file("./day6/day6-input.txt")
    for i in range(len(raw_data)):
        characters = 4
        batch = raw_data[(i - characters):i]
        if len(set(batch)) == characters:
            return i


def get_day6_results_for_second_part():
    raw_data = read_file("./day6/day6-input.txt")
    for i in range(len(raw_data)):
        characters = 14
        batch = raw_data[(i - characters):i]
        if len(set(batch)) == characters:
            return i
