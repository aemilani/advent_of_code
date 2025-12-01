import numpy as np


def is_valid_move(x, y, prev_value, visited, matrix):
    """Check if a move is valid."""
    return (0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1] and
            matrix[x, y] == prev_value + 1 and (x, y) not in visited)


def dfs(x, y, path, visited, results, matrix, directions):
    """Perform Depth-First Search to find paths."""
    if matrix[x, y] == 9:  # Path reaches 9
        results.append(path[:])
        return

    visited.add((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, matrix[x, y], visited, matrix):
            path.append((nx, ny))
            dfs(nx, ny, path, visited, results, matrix, directions)
            path.pop()
    visited.remove((x, y))


if __name__ == "__main__":
    with open('../../data/2024/10.txt', 'r') as f:
        string = f.read().strip()

    mat = np.array([list(line) for line in string.split('\n')]).astype(int)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    zero_inds = [(int(coord[0]), int(coord[1])) for coord in list(np.argwhere(mat == 0))]

    sum_scores = 0
    for coord in zero_inds:
        results = []
        visited = set()

        dfs(coord[0], coord[1], [(coord[0], coord[1])], visited, results, mat, directions)
        sum_scores += len(set([path[-1] for path in results]))

    print(f'part 1: {sum_scores}')

    sum_scores = 0
    for coord in zero_inds:
        results = []
        visited = set()

        dfs(coord[0], coord[1], [(coord[0], coord[1])], visited, results, mat, directions)
        sum_scores += len(results)

    print(f'part 2: {sum_scores}')
