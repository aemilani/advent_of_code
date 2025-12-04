def part_1(input_string: str) -> int:
    l = input_string.split('\n')

    output = 0
    for bank in l:
        j1 = max(bank[:-1], key=int)
        j1_index = bank.index(j1)
        j2 = max(bank[j1_index + 1:], key=int)
        output += int(j1 + j2)

    return output


def part_2(input_string: str) -> int:
    l = input_string.split('\n')

    output = 0
    for bank in l:
        jolt = ''
        for i in range(12, 1, -1):
            j = max(bank[:-i + 1], key=int)
            jolt += j
            j_index = bank.index(j)
            bank = bank[j_index + 1:]
        jolt += max(bank, key=int)
        output += int(jolt)

    return output


if __name__ == '__main__':
    with open('../../data/2025/03.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
