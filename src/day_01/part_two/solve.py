def solve(input_data: list[str]):
    current = 50
    sol = 0
    for entry in input_data:
        direction = entry[0]
        value = int(entry[1:])
        for _ in range(value):
            if direction == "L":
                current = (current - 1 + 100) % 100
            elif direction == "R":
                current = (current + 1) % 100
            else:
                assert False
            if current == 0:
                sol += 1
    print(sol)
