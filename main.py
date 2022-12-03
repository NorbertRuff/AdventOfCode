from day1 import get_results_for_first_part, get_results_for_second_part
from day2 import get_day2_results_for_first_part, get_day2_results_for_second_part
from day3 import get_day3_results_for_first_part, get_day3_results_for_second_part


def main():
    elf_calories = get_results_for_first_part()
    # print("day 1 first part result", max(elf_calories))
    # sum_of_calories_for_first_3_elf = get_results_for_second_part(elf_calories)
    # print("day 1 second part result", sum_of_calories_for_first_3_elf)
    # print("day 2 first part result", get_day2_results_for_first_part())
    # print("day 2 second part result", get_day2_results_for_second_part())
    # print("day 3 first part result", get_day3_results_for_first_part())
    print("day 3 second part result", get_day3_results_for_second_part())



if __name__ == '__main__':
    main()
