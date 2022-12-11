from day1 import get_results_for_first_part, get_results_for_second_part
from day10 import get_day10_part1_results, get_day10_part2_results
from day11 import get_day11_part2_results, get_day11_part1_results
from day2 import get_day2_results_for_first_part, get_day2_results_for_second_part
from day3 import get_day3_results_for_first_part, get_day3_results_for_second_part
from day4 import get_day4_results_for_first_part, get_day4_results_for_second_part
from day5 import get_day5_results_for_first_part, get_day5_results_for_second_part
from day6 import get_day6_results_for_first_part, get_day6_results_for_second_part
from day7 import get_day7_results
from day8 import get_day8_part1_results, get_day8_part2_results
from day9 import get_day9_part1_results, get_day9_part2_results


def main():
    elf_calories = get_results_for_first_part()
    print("day 1 first part result", max(elf_calories))
    print("day 1 second part result", get_results_for_second_part(elf_calories))

    print("day 2 first part result", get_day2_results_for_first_part())
    print("day 2 second part result", get_day2_results_for_second_part())

    print("day 3 first part result", get_day3_results_for_first_part())
    print("day 3 second part result", get_day3_results_for_second_part())

    print("day 4 first part result", get_day4_results_for_first_part())
    print("day 4 second part result", get_day4_results_for_second_part())

    print("day 5 first part result", get_day5_results_for_first_part())
    print("day 5 second part result", get_day5_results_for_second_part())

    print("day 6 first part result", get_day6_results_for_first_part())
    print("day 6 second part result", get_day6_results_for_second_part())

    print("day 7 result", get_day7_results())

    print("day 8 first part result", get_day8_part1_results())
    print("day 8 second part result", get_day8_part2_results())

    print("day 9 first part result", get_day9_part1_results())
    print("day 9 second part result", get_day9_part2_results())

    print("day 10 first part result", get_day10_part1_results())
    print("day 10 second part result", get_day10_part2_results())

    print("day 11 first part result", get_day11_part1_results())
    print("day 11 second part result", get_day11_part2_results())


if __name__ == '__main__':
    main()
