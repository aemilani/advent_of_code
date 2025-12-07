def part_1(input_string: str) -> int:
    ranges = input_string.split('\n\n')[0].split('\n')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]
    ingredients = input_string.split('\n\n')[1].split('\n')
    ingredients = [int(i) for i in ingredients]

    n_fresh = 0
    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                n_fresh += 1
                break
    return n_fresh


def part_2(input_string: str) -> int:
    ranges = input_string.split('\n\n')[0].split('\n')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]
    ranges = sorted(ranges)

    merged = []
    for a, b in ranges:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))

    sum_lengths = 0
    for a, b in merged:
        sum_lengths += (b - a + 1)
    return sum_lengths


if __name__ == '__main__':
    with open('../../data/2025/05.txt', 'r') as f:
        string = f.read().strip()
    # string = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
