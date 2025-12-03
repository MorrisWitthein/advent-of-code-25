def find_max(sub_list: list[int], offset: int):
    max_ = max(sub_list)
    return max_, sub_list.index(max_) + offset


def solve(input_data: list[str]):
    sol = 0
    for line in input_data:
        number = ""
        max_index = -1
        for i in range(11, -1, -1):
            end = len(line) - i
            digits = [int(d) for d in line[max_index + 1 : end]]
            max_value, max_index = find_max(digits, max_index + 1)
            number += str(max_value)
        print(number)
        sol += int(number)
    print(sol)
