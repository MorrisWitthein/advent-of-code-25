def check_row(line: str, col: int):
    count = 0
    for i in [col - 1, col, col + 1]:
        if 0 <= i < len(line):
            count += line[i] == "@"
    return count


def count_neighboring_roles(row: int, col: int, input_data: list[str]):
    count = check_row(input_data[row], col) - 1
    if row - 1 >= 0:
        count += check_row(input_data[row - 1], col)
    if row + 1 < len(input_data):
        count += check_row(input_data[row + 1], col)
    return count
