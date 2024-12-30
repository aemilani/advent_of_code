import numpy as np
from collections import deque
from typing import List, Tuple, Set


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_valid_move(x: int, y: int, seen: Set[Tuple[int, int]], mat: np.array) -> bool:
    return 0 <= x < mat.shape[0] and 0 <= y < mat.shape[1] and mat[x, y] == '.' and (x, y) not in seen


def find_shortest_path(mat: np.array) -> None | List[Tuple[int, int]]:
    start = (0, 0)
    end = (mat.shape[0] - 1, mat.shape[1] - 1)

    stack = deque()
    stack.append((start, [start]))
    seen = set()
    seen.add(start)

    paths = []
    while stack:
        (x, y), path = stack.popleft()
        if (x, y) == end:
            paths.append(path)
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, seen, mat):
                seen.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    if len(paths) == 0:
        return None

    path_lengths = []
    for path in paths:
        path_lengths.append(len(path))
    min_length = min(path_lengths)

    return paths[path_lengths.index(min_length)]


if __name__ == "__main__":
    with open('../../data/input/18.txt', 'r') as f:
        string = f.read().strip()

    coordinates = [(int(row.split(',')[1]), int(row.split(',')[0])) for row in string.split('\n')]

    grid_shape = (71, 71)
    grid = np.array([['.' for i in range(grid_shape[0])] for j in range(grid_shape[1])])

    for i in range(1024):
        byte_loc = coordinates[i]
        grid[byte_loc] = '#'

    shortest_path = find_shortest_path(grid)

    print(f'Part 1: {len(shortest_path) - 1}')

    blocking_coordinates = None
    for i in range(1024, len(coordinates)):
        print(f'{i}/{len(coordinates)}')
        byte_loc = coordinates[i]
        grid[byte_loc] = '#'
        shortest_path = find_shortest_path(grid)
        if not shortest_path:
            blocking_coordinates = byte_loc
            break

    print(f'Part 2: {blocking_coordinates[1]},{blocking_coordinates[0]}')
