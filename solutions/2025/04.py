from typing import List, Tuple


def neighbours(coord: Tuple[int, int], shape: Tuple[int, int]) -> List[Tuple[int, int]]:
    h, w = coord
    n = []
    for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if 0 <= h + dh < shape[1] and 0 <= w + dw < shape[0]:
            n.append((h + dh, w + dw))
    return n


def part_1(input_string: str) -> int:
    l = input_string.split('\n')
    mat = []
    for line in l:
        mat.append(list(line))
    h = len(mat)
    w = len(mat[0])
    n_access = 0
    for i in range(h):
        for j in range(w):
            elem = mat[i][j]
            if elem == '@':
                neighbour_list = neighbours((i, j), (h, w))
                neighbour_rolls = 0
                for ni, nj in neighbour_list:
                    if mat[ni][nj] == '@':
                        neighbour_rolls += 1
                if neighbour_rolls < 4:
                    n_access += 1
    return n_access


def part_2(input_string: str) -> int:
    l = input_string.split('\n')
    mat = []
    for line in l:
        mat.append(list(line))
    h = len(mat)
    w = len(mat[0])
    n_removed = 0
    removed = True
    while removed:
        removed = False
        for i in range(h):
            for j in range(w):
                elem = mat[i][j]
                if elem == '@':
                    neighbour_list = neighbours((i, j), (h, w))
                    neighbour_rolls = 0
                    for ni, nj in neighbour_list:
                        if mat[ni][nj] == '@':
                            neighbour_rolls += 1
                    if neighbour_rolls < 4:
                        n_removed += 1
                        mat[i][j] = '.'
                        removed = True
    return n_removed


if __name__ == '__main__':
    with open('../../data/2025/04.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
