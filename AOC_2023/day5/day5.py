import re

from utils import read_file_no_strip


def get_start_index(regex, data):
    return [i for i, line in enumerate(data) if regex.search(line)][0]


def make_list_of_start_and_end_index(start_number, end_number):
    return [i for i in range(start_number, start_number + end_number)]


def split_data_to_groups(raw_data):
    raw_data = [line.split(' ') for line in raw_data]
    raw_data = [[int(num) for num in line] for line in raw_data]
    raw_data_dict = {}
    for i in range(len(raw_data)):
        for j in range(raw_data[i][2]):
            raw_data_dict[raw_data[i][1] + j] = raw_data[i][0] + j
    return raw_data_dict


def get_seeds(raw_data):
    seeds_regex = re.compile(r'seeds:')
    seeds = [line for line in raw_data if seeds_regex.search(line)][0]
    seeds = seeds.split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    return seeds


def part1_resolver(raw_data):
    ## find seeds

    seed_to_soil_regex = re.compile(r'seed-to-soil map:')
    soil_to_fertilizer_regex = re.compile(r'soil-to-fertilizer map:')
    fertilizer_to_water_regex = re.compile(r'fertilizer-to-water map:')
    water_to_light_regex = re.compile(r'water-to-light map:')
    light_to_temperature_regex = re.compile(r'light-to-temperature map:')
    temperature_to_humidity_regex = re.compile(r'temperature-to-humidity map:')
    humidity_to_location_regex = re.compile(r'humidity-to-location map:')

    seed_to_soil_index = get_start_index(seed_to_soil_regex, raw_data)
    soil_to_fertilizer_index = get_start_index(soil_to_fertilizer_regex, raw_data)
    fertilizer_to_water_index = get_start_index(fertilizer_to_water_regex, raw_data)
    water_to_light_index = get_start_index(water_to_light_regex, raw_data)
    light_to_temperature_index = get_start_index(light_to_temperature_regex, raw_data)
    temperature_to_humidity_index = get_start_index(temperature_to_humidity_regex, raw_data)
    humidity_to_location_index = get_start_index(humidity_to_location_regex, raw_data)

    seeds = get_seeds(raw_data)

    seed_to_soil = raw_data[seed_to_soil_index + 1:soil_to_fertilizer_index - 1]
    seed_to_soil = split_data_to_groups(seed_to_soil)

    soil_to_fertilizer = raw_data[soil_to_fertilizer_index + 1:fertilizer_to_water_index - 1]
    soil_to_fertilizer = split_data_to_groups(soil_to_fertilizer)

    fertilizer_to_water = raw_data[fertilizer_to_water_index + 1:water_to_light_index - 1]
    fertilizer_to_water = split_data_to_groups(fertilizer_to_water)

    water_to_light = raw_data[water_to_light_index + 1:light_to_temperature_index - 1]
    water_to_light = split_data_to_groups(water_to_light)

    light_to_temperature = raw_data[light_to_temperature_index + 1:temperature_to_humidity_index - 1]
    light_to_temperature = split_data_to_groups(light_to_temperature)

    temperature_to_humidity = raw_data[temperature_to_humidity_index + 1:humidity_to_location_index - 1]
    temperature_to_humidity = split_data_to_groups(temperature_to_humidity)

    humidity_to_location = raw_data[humidity_to_location_index + 1:len(raw_data) - 2]
    humidity_to_location = split_data_to_groups(humidity_to_location)

    print('seeds', seeds)
    print('<---------------------------->')
    locations = []
    for seed in seeds:
        soil = seed_to_soil[seed] if seed in seed_to_soil else seed
        fertilizer = soil_to_fertilizer[soil] if soil in soil_to_fertilizer else soil
        water = fertilizer_to_water[fertilizer] if fertilizer in fertilizer_to_water else fertilizer
        light = water_to_light[water] if water in water_to_light else water
        temperature = light_to_temperature[light] if light in light_to_temperature else light
        humidity = temperature_to_humidity[temperature] if temperature in temperature_to_humidity else temperature
        location = humidity_to_location[humidity] if humidity in humidity_to_location else humidity
        print(seed, location)
        locations.append(location)
        print('<---------------------------->')
    print('min', min(locations))
    return min(locations)


def part2_resolver(raw_data):
    ## find seeds

    seed_to_soil_regex = re.compile(r'seed-to-soil map:')
    soil_to_fertilizer_regex = re.compile(r'soil-to-fertilizer map:')
    fertilizer_to_water_regex = re.compile(r'fertilizer-to-water map:')
    water_to_light_regex = re.compile(r'water-to-light map:')
    light_to_temperature_regex = re.compile(r'light-to-temperature map:')
    temperature_to_humidity_regex = re.compile(r'temperature-to-humidity map:')
    humidity_to_location_regex = re.compile(r'humidity-to-location map:')

    seed_to_soil_index = get_start_index(seed_to_soil_regex, raw_data)
    soil_to_fertilizer_index = get_start_index(soil_to_fertilizer_regex, raw_data)
    fertilizer_to_water_index = get_start_index(fertilizer_to_water_regex, raw_data)
    water_to_light_index = get_start_index(water_to_light_regex, raw_data)
    light_to_temperature_index = get_start_index(light_to_temperature_regex, raw_data)
    temperature_to_humidity_index = get_start_index(temperature_to_humidity_regex, raw_data)
    humidity_to_location_index = get_start_index(humidity_to_location_regex, raw_data)

    seeds = get_seeds(raw_data)

    seed_to_soil = raw_data[seed_to_soil_index + 1:soil_to_fertilizer_index - 1]
    seed_to_soil = split_data_to_groups(seed_to_soil)

    soil_to_fertilizer = raw_data[soil_to_fertilizer_index + 1:fertilizer_to_water_index - 1]
    soil_to_fertilizer = split_data_to_groups(soil_to_fertilizer)

    fertilizer_to_water = raw_data[fertilizer_to_water_index + 1:water_to_light_index - 1]
    fertilizer_to_water = split_data_to_groups(fertilizer_to_water)

    water_to_light = raw_data[water_to_light_index + 1:light_to_temperature_index - 1]
    water_to_light = split_data_to_groups(water_to_light)

    light_to_temperature = raw_data[light_to_temperature_index + 1:temperature_to_humidity_index - 1]
    light_to_temperature = split_data_to_groups(light_to_temperature)

    temperature_to_humidity = raw_data[temperature_to_humidity_index + 1:humidity_to_location_index - 1]
    temperature_to_humidity = split_data_to_groups(temperature_to_humidity)

    humidity_to_location = raw_data[humidity_to_location_index + 1:len(raw_data) - 2]
    humidity_to_location = split_data_to_groups(humidity_to_location)

    print('seeds', seeds)
    print('<---------------------------->')
    locations = []
    for i in range(seeds[0], seeds[1] + 1):
        soil = seed_to_soil[seeds[i]] if seeds[i] in seed_to_soil else seeds[i]
        fertilizer = soil_to_fertilizer[soil] if soil in soil_to_fertilizer else soil
        water = fertilizer_to_water[fertilizer] if fertilizer in fertilizer_to_water else fertilizer
        light = water_to_light[water] if water in water_to_light else water
        temperature = light_to_temperature[light] if light in light_to_temperature else light
        humidity = temperature_to_humidity[temperature] if temperature in temperature_to_humidity else temperature
        location = humidity_to_location[humidity] if humidity in humidity_to_location else humidity
        print(seeds[i], location)
        locations.append(location)
        print('<---------------------------->')

    for i in range(seeds[2], seeds[2] + 1):
        soil = seed_to_soil[seeds[i]] if seeds[i] in seed_to_soil else seeds[i]
        fertilizer = soil_to_fertilizer[soil] if soil in soil_to_fertilizer else soil
        water = fertilizer_to_water[fertilizer] if fertilizer in fertilizer_to_water else fertilizer
        light = water_to_light[water] if water in water_to_light else water
        temperature = light_to_temperature[light] if light in light_to_temperature else light
        humidity = temperature_to_humidity[temperature] if temperature in temperature_to_humidity else temperature
        location = humidity_to_location[humidity] if humidity in humidity_to_location else humidity
        print(seeds[i], location)
        locations.append(location)
        print('<---------------------------->')
    print('min', min(locations))

    return min(locations)


if __name__ == '__main__':
    raw_data = read_file_no_strip('./input.txt').splitlines()
    first_part_result = part1_resolver(raw_data)
    print('first_part_result', first_part_result)
    second_part_result = part2_resolver(raw_data)
    print('second_part_result', second_part_result)
