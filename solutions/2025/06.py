from math import prod
import re


def part_1(input_string: str) -> int:
    lines = [list(filter(None, line.strip().split(' '))) for line in input_string.splitlines()]
    numbers = lines[:-1]
    ops = lines[-1]
    result = 0
    for col in range(len(ops)):
        nums = [int(num_list[col]) for num_list in numbers]
        if ops[col] == '+':
            result += sum(nums)
        else:
            result += prod(nums)
    return result


def part_2(input_string: str) -> int:
    lines = input_string.splitlines()
    numbers = lines[:-1]
    ops = lines[-1]
    lens = [len(elem) for elem in re.split(r'[*+]', ops)[1:]]
    lens[-1] += 1
    ops = list(filter(None, ops.strip().split(' ')))

    clean_numbers = []
    for line in numbers:
        num = []
        idx = 0
        for l in lens:
            num.append(line[idx:idx + l])
            idx += (l + 1)
        clean_numbers.append(num)

    result = 0
    for col in range(len(ops)):
        nums = [num_list[col] for num_list in clean_numbers]
        n = []
        for i in range(lens[col]):
            n.append(int(''.join([num[i] for num in nums])))

        if ops[col] == '+':
            result += sum(n)
        else:
            result += prod(n)
    return result


if __name__ == '__main__':
    with open('../../data/2025/06.txt', 'r') as f:
        string = f.read()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
