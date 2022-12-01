
def read_file(filename):
    try:
        with open(filename) as f:
            data = f.read().strip()
    except FileNotFoundError:
        raise Exception("File not found")
    return data

