def id_in_range(lower: int, upper: int, id_: int):
    return lower <= id_ <= upper


def solve(input_data: str):
    raw_ranges, raw_ids = input_data.split("\n\n")
    ranges = [(int(x), int(y)) for x, y in (r.split("-") for r in raw_ranges.splitlines())]
    ids = [int(i) for i in raw_ids.splitlines()]
    sol = 0
    for id_ in ids:
        if any(id_in_range(lower, upper, id_) for (lower, upper) in ranges):
            sol += 1
    print(sol)
