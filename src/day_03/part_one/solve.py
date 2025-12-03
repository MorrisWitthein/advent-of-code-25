def solve(input_data: list[str]):
    sol = 0
    for line in input_data:
        digits = [int(d) for d in line[:-1]]
        left_max = max(digits)
        max_index = digits.index(left_max)
        digits = [int(d) for d in line[max_index + 1:]]
        right_max = max(digits)
        sol += int(str(left_max) + str(right_max))
    print(sol)
