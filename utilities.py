def get_file_lines(file) -> int:
    with open(file, 'r') as file: lines = len(file.readlines())
    return lines

