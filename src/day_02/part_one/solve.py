def solve(input_data: list[str]):
    sol = 0
    for range_ in input_data[0].split(","):
        l, r = (int(range_.split("-")[0]), int(range_.split("-")[1]))
        for i in range(l, r + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            mid = int(len(s) / 2)
            if s[:mid] == s[mid:]:
                sol += i
    print(sol)
