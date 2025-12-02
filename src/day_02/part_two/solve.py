def solve(input_data: list[str]):
    sol = 0
    for range_ in input_data[0].split(","):
        l, r = (int(range_.split("-")[0]), int(range_.split("-")[1]))
        for i in range(l, r + 1):
            s = str(i)
            mid = int(len(s) / 2)
            for j in range(1, mid + 1):
                if len(s) % j != 0:
                    continue
                current = j
                found = True
                while current + j <= len(s):
                    if s[current - j: current] != s[current: current + j]:
                        found = False
                        break
                    current += j
                if found:
                    sol += i
                    break
    print(sol)
