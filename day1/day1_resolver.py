from typing import List
from utils import read_file


# sum of calories for each elf in the list
# 1. get the data
# 2. split the data into groups
# 3. sum the calories for each group
# 4. sort the list
def get_results_for_first_part() -> list:
    raw_data = read_file("./day1/day1-input.txt").splitlines()
    elf_calories: List[int] = []
    sum_of_one_elf_calories = 0

    for i in range(len(raw_data)):
        if raw_data[i] == "":
            elf_calories.append(sum_of_one_elf_calories)
            sum_of_one_elf_calories = 0
        else:
            sum_of_one_elf_calories += int(raw_data[i])
    elf_calories.append(sum_of_one_elf_calories)

    elf_calories.sort(reverse=True)
    return elf_calories


# sum of calories for first 3 elf
def get_results_for_second_part(elf_calories: list) -> int:
    print(elf_calories[:3])
    return sum(elf_calories[:3])
