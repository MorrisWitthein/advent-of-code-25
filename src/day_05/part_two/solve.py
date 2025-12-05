def ranges_overlap(first, second):
    l1, r1 = first
    l2, r2 = second
    return l1 <= r2 and l2 <= r1


def solve(input_data: str):
    raw_ranges, _ = input_data.split("\n\n")
    ranges = [
        (int(x), int(y)) for x, y in (r.split("-") for r in raw_ranges.splitlines())
    ]
    sol = 0
    while True:
        for i, range_ in enumerate(ranges):
            changed = False
            for j in range(i + 1, len(ranges)):
                next_ = ranges[j]
                if ranges_overlap(range_, next_):
                    ranges.append((min(range_[0], next_[0]), max(range_[1], next_[1])))
                    del ranges[j]
                    del ranges[i]
                    changed = True
                    break
            if changed:
                break
        else:
            break
    for lower, upper in ranges:
        sol += abs(upper - lower) + 1
    print(sol)
