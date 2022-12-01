from day1 import get_results_for_first_part, get_results_for_second_part


def main():
    elf_calories = get_results_for_first_part()
    print(max(elf_calories))
    sum_of_calories_for_first_3_elf = get_results_for_second_part(elf_calories)
    print(sum_of_calories_for_first_3_elf)


if __name__ == '__main__':
    main()
