from typing import List
from collections import deque


def splitter_indices(line: str) -> List[int]:
    indices = []
    for i, space in enumerate(line):
        if space == '^':
            indices.append(i)
    return indices


def part_1(input_string: str) -> int:
    lines = input_string.split('\n')
    start = lines[0].index('S')
    beam_cols = {start}
    n_split = 0
    for line in lines[1:]:
        splitter_ids = splitter_indices(line)
        if splitter_ids:
            for splitter_id in splitter_ids:
                if splitter_id in beam_cols:
                    n_split += 1
                    beam_cols.remove(splitter_id)
                    beam_cols.add(splitter_id - 1)
                    beam_cols.add(splitter_id + 1)
    return n_split


def part_2(input_string: str) -> int:
    lines = input_string.split('\n')
    start = lines[0].index('S')
    beams = [0 for _ in range(len(lines[0]))]
    beams[start] += 1
    for line in lines[1:]:
        splitter_ids = splitter_indices(line)
        if splitter_ids:
            for splitter_id in splitter_ids:
                if beams[splitter_id] != 0:
                    beams[splitter_id + 1] += beams[splitter_id]
                    beams[splitter_id - 1] += beams[splitter_id]
                    beams[splitter_id] = 0
    return sum(beams)


if __name__ == '__main__':
    with open('../../data/2025/07.txt', 'r') as f:
        string = f.read()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')