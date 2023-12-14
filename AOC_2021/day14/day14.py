import math

from collections import Counter


def load_file():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    return lines


def get_pairs(lines):
    pairs = {}
    for line in lines[2:]:
        (start, end) = line.split(' -> ')
        pairs[start] = end
    return pairs


def main():
    lines = load_file()
    start_string = lines[0]
    pairs = get_pairs(lines)
    print(pairs)

    pairs_counter = Counter()
    for i in range(len(start_string) - 1):
        pairs_counter[start_string[i:i+2]] += 1

    step = 0
    while step < 40:
        old_pairs = pairs_counter.copy()
        print(old_pairs)
        for i, j in old_pairs.items():
            if j > 0:
                pairs_counter[i] -= j
                ins = pairs[i]
                pairs_counter[i[0] + ins] += j
                pairs_counter[ins + i[1]] += j
                print(ins)
        step += 1
        if step == 10:
            counts = Counter()
            for i, j in pairs_counter.items():
                counts[i[0]] += j / 2
                counts[i[1]] += j / 2
            print(math.ceil(counts.most_common()[0][1] - counts.most_common()[-1][1]))

    counts = Counter()
    for i, j in pairs_counter.items():
        counts[i[0]] += j / 2
        counts[i[1]] += j / 2
    print(math.ceil(counts.most_common()[0][1] - counts.most_common()[-1][1]))


if __name__ == '__main__':
    main()
