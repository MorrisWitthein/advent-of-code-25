from shared.shared import count_neighboring_roles


def solve(input_data: list[str]):
    sol = 0
    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char != "@":
                continue
            if count_neighboring_roles(i, j, input_data) < 4:
                sol += 1
    print(sol)
