from functools import cache


def part_1(input_string: str) -> int:
    patterns = input_string.split('\n\n')[0].split(', ')
    towels = input_string.split('\n\n')[1].split('\n')

    @cache
    def is_possible(towel: str) -> bool:
        return (towel == '' or
                any(towel.startswith(pattern) and is_possible(towel[len(pattern):]) for pattern in patterns))

    return sum(map(is_possible, towels))


def part_2(input_string: str) -> int:
    patterns = input_string.split('\n\n')[0].split(', ')
    towels = input_string.split('\n\n')[1].split('\n')

    @cache
    def n_possible(towel: str) -> int:
        if towel == '':
            return 1

        n = 0
        for pattern in patterns:
            if towel.startswith(pattern):
                n += n_possible(towel[len(pattern):])

        return n

    return sum(map(n_possible, towels))


if __name__ == "__main__":
    with open('../../data/2024/19.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')

    print(f'Part 2: {part_2(string)}')
