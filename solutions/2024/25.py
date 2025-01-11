from typing import List


def get_heights(schematic: str) -> List[int]:
    h = []
    for i in range(len(schematic.split('\n')[0])):
        h.append(0)
    for row in schematic.split('\n'):
        for i, char in enumerate(row):
            if char == '#':
                h[i] += 1
    return h


def fit(key: str, lock: str) -> bool:
    h_key = len(key.split('\n'))
    h_lock = len(lock.split('\n'))
    if h_key != h_lock:
        return False
    for h1, h2 in zip(get_heights(key), get_heights(lock)):
        if h1 + h2 > h_key:
            return False
    return True


def part_1(input_string: str) -> int:
    locks = [s for s in input_string.split('\n\n') if s[0] == '#']
    keys = [s for s in input_string.split('\n\n') if s[0] == '.']
    n = 0
    for k in keys:
        for l in locks:
            if fit(k, l):
                n += 1
    return n


if __name__ == '__main__':
    with open('../../data/input/25.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
