import numpy as np
from typing import List, Tuple


def gps(box_h: int, box_w: int) -> int:
    return 100 * box_h + box_w


def calc_gps_sum(mat: np.array) -> int:
    gps_sum = 0
    for h, w in np.argwhere(mat == 'O'):
        gps_sum += gps(h, w)
    return gps_sum


def calc_gps_sum_wide(mat: np.array) -> int:
    gps_sum = 0
    for h, w in np.argwhere(mat == '['):
        gps_left = gps(h, w)
        gps_right = gps(h, w + 1)
        gps_sum += min(gps_left, gps_right)
    return gps_sum


def move_right(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]
    first_wall_w = np.argwhere(mat[robot_h, robot_w + 1:] == '#')[0][0] + robot_w + 1
    path = mat[robot_h, robot_w:first_wall_w]
    if '.' in path:
        first_space = np.argwhere(path == '.')[0][0]
        path[:first_space + 1] = np.concat([np.array(['.']), path[:first_space]])
    return mat


def move_down(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]
    first_wall_h = np.argwhere(mat[robot_h + 1:, robot_w] == '#')[0][0] + robot_h + 1
    path = mat[robot_h:first_wall_h, robot_w]
    if '.' in path:
        first_space = np.argwhere(path == '.')[0][0]
        path[:first_space + 1] = np.concat([np.array(['.']), path[:first_space]])
    return mat


def move_down_wide(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]

    if mat[robot_h + 1, robot_w] == '.':
        mat[robot_h, robot_w] = '.'
        mat[robot_h + 1, robot_w] = '@'
        return mat

    first_wall_h = np.argwhere(mat[robot_h + 1:, robot_w] == '#')[0][0] + robot_h + 1
    path = mat[robot_h:first_wall_h, robot_w]

    if '.' not in path:
        return mat

    def search_boxes(h, w, paths_coordinates, path_starts):
        if (h, w) in path_starts:
            return
        path_starts.append((h, w))
        path = [(h, w)]
        while True:
            if mat[h, w] == '.' or mat[h, w] == '#':
                paths_coordinates.append(path)
                return
            elif mat[h, w] == '[':
                search_boxes(h, w + 1, paths_coordinates, path_starts)
            elif mat[h, w] == ']':
                search_boxes(h, w - 1, paths_coordinates, path_starts)
            h += 1
            path.append((h, w))

    path_coordinates = []
    path_starts = []
    search_boxes(robot_h, robot_w, path_coordinates, path_starts)

    paths = []
    for lis in path_coordinates:
        h_end, w_end = lis[-1]
        h_start, w_start = lis[0]
        paths.append(mat[h_start:h_end + 1, w_start])

    for path in paths:
        if '.' not in path:
            return mat

    for path in paths:
        first_space = np.argwhere(path == '.')[0][0]
        path[:first_space + 1] = np.concat([np.array(['.']), path[:first_space]])

    return mat


def move_left(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]
    first_wall_w = np.argwhere(mat[robot_h, :robot_w] == '#')[-1][0]
    path = mat[robot_h, first_wall_w + 1:robot_w + 1]
    if '.' in path:
        first_space = np.argwhere(path == '.')[-1][0]
        path[first_space:] = np.concat([path[first_space + 1:], np.array(['.'])])
    return mat


def move_up(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]
    first_wall_h = np.argwhere(mat[:robot_h, robot_w] == '#')[-1][0]
    path = mat[first_wall_h + 1:robot_h + 1, robot_w]
    if '.' in path:
        first_space = np.argwhere(path == '.')[-1][0]
        path[first_space:] = np.concat([path[first_space + 1:], np.array(['.'])])
    return mat


def move_up_wide(mat: np.array) -> np.array:
    robot_h, robot_w = np.argwhere(mat == '@')[0][0], np.argwhere(mat == '@')[0][1]

    if mat[robot_h - 1, robot_w] == '.':
        mat[robot_h, robot_w] = '.'
        mat[robot_h - 1, robot_w] = '@'
        return mat

    first_wall_h = np.argwhere(mat[:robot_h, robot_w] == '#')[-1][0]
    path = mat[first_wall_h + 1:robot_h + 1, robot_w]

    if '.' not in path:
        return mat

    def search_boxes(h, w, paths_coordinates, path_starts):
        if (h, w) in path_starts:
            return
        path_starts.append((h, w))
        path = [(h, w)]
        while True:
            if mat[h, w] == '.' or mat[h, w] == '#':
                paths_coordinates.append(path)
                return
            elif mat[h, w] == '[':
                search_boxes(h, w + 1, paths_coordinates, path_starts)
            elif mat[h, w] == ']':
                search_boxes(h, w - 1, paths_coordinates, path_starts)
            h -= 1
            path.append((h, w))

    path_coordinates = []
    path_starts = []
    search_boxes(robot_h, robot_w, path_coordinates, path_starts)

    paths = []
    for lis in path_coordinates:
        h_end, w_end = lis[0]
        h_start, w_start = lis[-1]
        paths.append(mat[h_start:h_end + 1, w_start])

    for path in paths:
        if '.' not in path:
            return mat

    for path in paths:
        first_space = np.argwhere(path == '.')[-1][0]
        path[first_space:] = np.concat([path[first_space + 1:], np.array(['.'])])

    return mat


def step_robot(move: str, mat: np.array) -> np.array:
    if move == '>':
        return move_right(mat)
    if move == 'v':
        return move_down(mat)
    if move == '<':
        return move_left(mat)
    if move == '^':
        return move_up(mat)


def step_robot_wide(move: str, mat: np.array) -> np.array:
    if move == '>':
        return move_right(mat)
    if move == 'v':
        return move_down_wide(mat)
    if move == '<':
        return move_left(mat)
    if move == '^':
        return move_up_wide(mat)


def run(all_moves: str, mat: np.array) -> np.array:
    mat_copy = mat.copy()
    for move in all_moves:
        mat_copy = step_robot(move, mat_copy)
    return mat_copy


def run_wide(all_moves: str, mat: np.array) -> np.array:
    mat_copy = mat.copy()
    for move in all_moves:
        mat_copy = step_robot_wide(move, mat_copy)
    return mat_copy


def get_map_str(mat: np.array) -> np.array:
    st = ''
    for i in range(mat.shape[0]):
        line = mat[i, :]
        for elem in line:
            st += elem
        st += '\n'
    return st


if __name__ == "__main__":
    with open('../../data/2024/15.txt', 'r') as f:
        string = f.read().strip()

    warehouse_str = string.split('\n\n')[0].strip()
    moves = string.split('\n\n')[1].strip().replace('\n', '')

    warehouse_mat = np.array([list(line) for line in warehouse_str.split('\n')])
    final_warehouse_mat = run(moves, warehouse_mat)
    sum_gps_coordinates = calc_gps_sum(final_warehouse_mat)

    print(f'Part 1: {sum_gps_coordinates}')

    new_warehouse_str = warehouse_str.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

    new_warehouse_mat = np.array([list(line) for line in new_warehouse_str.split('\n')])
    final_new_warehouse_mat = run_wide(moves, new_warehouse_mat)

    sum_gps_coordinates_wide = calc_gps_sum_wide(final_new_warehouse_mat)

    print(f'Part 2: {sum_gps_coordinates_wide}')
