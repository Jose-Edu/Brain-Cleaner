def get_file_lines(file) -> int:
    with open(file, 'r') as file: lines = len(file.readlines())
    return lines


def count_moves(bf_block) -> int:
    return bf_block.count(">") - bf_block.count("<")

