def solve(input_data: list[str]):
    current = 50
    sol = 0
    for entry in input_data:
        direction = entry[0]
        value = int(entry[1:])
        if direction == "L":
            current = (current - value) % 100
        elif direction == "R":
            current = (current + value) % 100
        else:
            assert False
        if current == 0:
            sol += 1
    print(sol)
