def part_1(input_string: str) -> int:
    l = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in input_string.split(',')]

    invalids = []
    for a, b in l:
        for n in range(a, b + 1):
            s = str(n)
            if len(s) % 2 == 0:
                if s[:len(s) // 2] == s[len(s) // 2:]:
                    invalids.append(int(s))

    return sum(invalids)


def part_2(input_string: str) -> int:
    l = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in input_string.split(',')]

    invalids = []
    for a, b in l:
        for n in range(a, b + 1):
            n_added = False
            s = str(n)
            for length in range(1, len(s) // 2 + 1):
                if len(s) % length == 0 and not n_added:
                    n_units = len(s) // length
                    chunks = [s[i * length: (i + 1) * length] for i in range(n_units)]
                    if len(set(chunks)) == 1:
                        invalids.append(n)
                        n_added = True

    return sum(invalids)


if __name__ == '__main__':
    with open('../../data/2025/02.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
