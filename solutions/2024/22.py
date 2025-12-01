import numpy as np
from typing import List


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def evolve_secret_number(a: int) -> int:
    a = prune(mix(a * 64, a))
    a = prune(mix(a // 32, a))
    a = prune(mix(a * 2048, a))
    return a


def generate_prices(seed: int, count: int) -> List[int]:
    out = [seed % 10]
    for _ in range(count):
        res = evolve_secret_number(seed)
        out.append(res % 10)
        seed = res
    return out


def calc_secret_number(seed: int, iters: int) -> int:
    a = seed
    for _ in range(iters):
        a = evolve_secret_number(a)
    return a


def part_1(input_string: str) -> int:
    sum_numbers = 0
    for num in input_string.strip().split('\n'):
        sum_numbers += calc_secret_number(int(num), 2000)
    return sum_numbers


def part_2(input_string: str) -> int:
    all_seq_nums = dict()
    for num in input_string.strip().split('\n'):
        unique_seqs = set()
        num = int(num)
        prices = generate_prices(num, 2000)
        diffs = np.array(prices)[1:] - np.array(prices)[:-1]
        for i in range(2000 - 4 + 1):
            seq = (diffs[i], diffs[i + 1], diffs[i + 2], diffs[i + 3])
            if seq not in unique_seqs:
                unique_seqs.add(seq)
                if seq not in all_seq_nums:
                    all_seq_nums[seq] = prices[i + 4]
                else:
                    all_seq_nums[seq] += prices[i + 4]

    return max(all_seq_nums.values())


if __name__ == '__main__':
    with open('../../data/2024/22.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')

    print(f'Part 2: {part_2(string)}')
