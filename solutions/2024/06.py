import numpy as np


def step_guard(mat, guard_symbol, guard_loc):
    turned = False
    if guard_symbol == '<':
        if mat[guard_loc[0], guard_loc[1] - 1] == '.' or mat[guard_loc[0], guard_loc[1] - 1] == 'X':
            mat[guard_loc[0], guard_loc[1] - 1] = guard_symbol
            mat[guard_loc[0], guard_loc[1]] = 'X'
            guard_loc = guard_loc[0], guard_loc[1] - 1
        elif mat[guard_loc[0], guard_loc[1] - 1] == '#':
            guard_symbol = '^'
            turned = True

    elif guard_symbol == '^':
        if mat[guard_loc[0] - 1, guard_loc[1]] == '.' or mat[guard_loc[0] - 1, guard_loc[1]] == 'X':
            mat[guard_loc[0] - 1, guard_loc[1]] = guard_symbol
            mat[guard_loc[0], guard_loc[1]] = 'X'
            guard_loc = guard_loc[0] - 1, guard_loc[1]
        elif mat[guard_loc[0] - 1, guard_loc[1]] == '#':
            guard_symbol = '>'
            turned = True

    elif guard_symbol == '>':
        if mat[guard_loc[0], guard_loc[1] + 1] == '.' or mat[guard_loc[0], guard_loc[1] + 1] == 'X':
            mat[guard_loc[0], guard_loc[1] + 1] = guard_symbol
            mat[guard_loc[0], guard_loc[1]] = 'X'
            guard_loc = guard_loc[0], guard_loc[1] + 1
        elif mat[guard_loc[0], guard_loc[1] + 1] == '#':
            guard_symbol = 'v'
            turned = True

    elif guard_symbol == 'v':
        if mat[guard_loc[0] + 1, guard_loc[1]] == '.' or mat[guard_loc[0] + 1, guard_loc[1]] == 'X':
            mat[guard_loc[0] + 1, guard_loc[1]] = guard_symbol
            mat[guard_loc[0], guard_loc[1]] = 'X'
            guard_loc = guard_loc[0] + 1, guard_loc[1]
        elif mat[guard_loc[0] + 1, guard_loc[1]] == '#':
            guard_symbol = '<'
            turned = True

    return mat, guard_symbol, guard_loc, turned


if __name__ == "__main__":
    with open('../../data/2024/06.txt', 'r') as f:
        string = f.read().strip()

    # string = ('....#.....\n.........#\n..........\n..#.......\n.......#..\n'
    #           '..........\n.#..^.....\n........#.\n#.........\n......#...')

    lis = string.split('\n')
    mat = np.array([list(elem) for elem in lis])

    symbols, counts = np.unique(mat, return_counts=True)
    guard_symbol = symbols[np.argwhere(counts == 1)[0][0]]
    guard_loc = int(np.argwhere(mat == guard_symbol)[0][0]), int(np.argwhere(mat == guard_symbol)[0][1])

    while guard_loc[0] != 0 and guard_loc[0] != (mat.shape[0] - 1) and \
            guard_loc[1] != 0 and guard_loc[1] != (mat.shape[0] - 1):
        mat, guard_symbol, guard_loc, _ = step_guard(mat, guard_symbol, guard_loc)

    mat[guard_loc[0], guard_loc[1]] = 'X'
    guard_path = np.int_(mat == 'X')
    n_visited = np.count_nonzero(guard_path)

    print(f'Part 1: {n_visited}')

    guard_path_coordinates = [(int(coord[0]), int(coord[1])) for coord in list(np.argwhere(guard_path == 1))]

    mat = np.array([list(elem) for elem in lis])  # Reset the map
    symbols, counts = np.unique(mat, return_counts=True)
    guard_symbol = symbols[np.argwhere(counts == 1)[0][0]]
    guard_loc = int(np.argwhere(mat == guard_symbol)[0][0]), int(np.argwhere(mat == guard_symbol)[0][1])

    guard_path_coordinates.remove(guard_loc)

    n_loops = 0
    for coord in guard_path_coordinates:
        print(coord)
        loop = False
        mat = np.array([list(elem) for elem in lis])  # Reset the map
        symbols, counts = np.unique(mat, return_counts=True)
        guard_symbol = symbols[np.argwhere(counts == 1)[0][0]]
        guard_loc = int(np.argwhere(mat == guard_symbol)[0][0]), int(np.argwhere(mat == guard_symbol)[0][1])

        mat[coord] = '#'
        turn_coords = []
        while guard_loc[0] != 0 and guard_loc[0] != (mat.shape[0] - 1) and \
                guard_loc[1] != 0 and guard_loc[1] != (mat.shape[0] - 1):
            mat, guard_symbol, guard_loc, turned = step_guard(mat, guard_symbol, guard_loc)
            if turned and (len(turn_coords) == 0 or turn_coords[-1] != guard_loc):
                turn_coords.append(guard_loc)
            for turn_coord in turn_coords:
                if turn_coords.count(turn_coord) != 1:
                    loop = True
            if loop:
                n_loops += 1
                break

    print(f'Part 2: {n_loops}')
