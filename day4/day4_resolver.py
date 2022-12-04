from utils import read_file_no_strip


def get_day4_results_for_first_part():
    raw_data = read_file_no_strip("./day4/day4-input.txt")
    total_elfs = 0
    for line in raw_data.splitlines():
        first_elf = line.split(",")[0].split('-')
        second_elf = line.split(",")[1].split('-')
        first_set = set(range(int(first_elf[0]), int(first_elf[1]) + 1))
        second_set = set(range(int(second_elf[0]), int(second_elf[1])+1))
        # https://stackoverflow.com/questions/70579609/check-a-given-range-of-values-is-present-in-another-range-values-in-python
        if second_set.issubset(first_set) or first_set.issubset(second_set):
            total_elfs += 1
    return total_elfs


def get_day4_results_for_second_part():
    raw_data = read_file_no_strip("./day4/day4-input.txt")
    elfs = []
    total_elfs = 0
    for line in raw_data.splitlines():
        first_elf = line.split(",")[0].split('-')
        second_elf = line.split(",")[1].split('-')
        first_list = list(set(range(int(first_elf[0]), int(first_elf[1]) + 1)))
        second_list = list(set(range(int(second_elf[0]), int(second_elf[1])+1)))
        elfs.append(first_list)
        elfs.append(second_list)
    for i in range(0, len(elfs), 2):
        first_elf = elfs[i]
        second_elf = elfs[i+1]
        if len(set(first_elf) & set(second_elf)) > 0:
            total_elfs += 1

    return total_elfs
