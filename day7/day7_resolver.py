from utils import read_file, read_file_no_strip

raw_data = read_file_no_strip("./day7/day7-input.txt")


def get_day7_results():
    current_directory = []
    directories = {}
    for line in raw_data.splitlines():
        total = 0
        x, command, *args = line.strip().split()
        args = args[0] if args else None
        if x != "$" and x != "dir":
            directory = '/'.join(current_directory)
            while directory:
                directories[directory][0] += int(x)
                directory = directories[directory][1]
        elif command == "cd":
            if args == "..":
                current_directory.pop()
            else:
                current_directory.append(args)
            directory = '/'.join(current_directory)
            if directory not in directories:
                directories[directory] = [0, '/'.join(current_directory[:-1])]
    total = sum(size for size, _ in directories.values() if size <= 100000)
    path = [size for size, _ in directories.values()]
    part_b = [size for size in sorted(path) if size >= 30000000 - (70000000 - directories["/"][0])][0]
    return total, part_b
