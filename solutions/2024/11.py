import numpy as np


def change(stone):
    if stone == '0':
        return '1'
    elif len(stone) % 2 == 0:
        return str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))
    else:
        return str(int(stone) * 2024)


def blink(stones):
    new_stones = []
    for stone in stones:
        output = change(stone)
        if isinstance(output, tuple):
            new_stones.extend(output)
        elif isinstance(output, str):
            new_stones.append(output)
    return new_stones


def blink_n_times(stones, n_times):
    for i in range(n_times):
        stones = blink(stones)
    return stones


if __name__ == "__main__":
    with open('../../data/input/11.txt', 'r') as f:
        string = f.read().strip()
    line = string.split()

    line = blink_n_times(line, 25)

    print(f'Part 1: {len(line)}')

    sum_lens = 0
    uniques, counts = np.unique(line, return_counts=True)
    iter = 1
    for stone1, ct1 in zip(uniques, counts):
        print(f'{iter} / {len(uniques)}')
        line_1 = blink_n_times([stone1], 25)
        uniques1, counts1 = np.unique(line_1, return_counts=True)
        for stone2, ct2 in zip(uniques1, counts1):
            line_2 = blink_n_times([stone2], 25)
            sum_lens += len(line_2) * ct1 * ct2
        iter += 1

    print(f'Part 2: {sum_lens}')
