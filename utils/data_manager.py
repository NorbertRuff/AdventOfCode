def read_file(filename):
    try:
        with open(filename) as f:
            data = f.read().strip()
    except FileNotFoundError:
        raise Exception("File not found")
    finally:
        f.close()
    return data


def read_file_no_strip(filename):
    try:
        with open(filename) as f:
            data = f.read()
    except FileNotFoundError:
        raise Exception("File not found")
    finally:
        f.close()
    return data
