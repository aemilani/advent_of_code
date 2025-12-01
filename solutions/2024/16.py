import numpy as np
from typing import Tuple, List
from collections import deque


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def calc_score(path: List[Tuple[int, int]]) -> int:
    score = 0
    dirs = [(0, 1)]
    for i in range(1, len(path)):
        diff = (path[i][0] - path[i - 1][0]), (path[i][1] - path[i - 1][1])
        dirs.append(diff)
    for i in range(1, len(dirs)):
        if dirs[i] == dirs[i - 1]:
            score += 1
        else:
            score += 1001
    return score


def turn_right(current_direction: Tuple[int, int]) -> Tuple[int, int]:
    return directions[(directions.index(current_direction) + 1) % len(directions)]


def turn_left(current_direction: Tuple[int, int]) -> Tuple[int, int]:
    return directions[(directions.index(current_direction) - 1 + len(directions)) % len(directions)]


def print_maze(maze: List[List[str]]):
    maze_str = ''
    for row in maze:
        row_str = ''
        for elem in row:
            row_str += str(elem).rjust(6)
        maze_str += row_str
        maze_str += '\n'
    print(maze_str)


if __name__ == "__main__":
    with open('../../data/2024/16.txt', 'r') as f:
        string = f.read().strip()

    maze = np.array([list(row) for row in string.split('\n')])

    start_point = int(np.argwhere(maze == 'S')[0][0]), int(np.argwhere(maze == 'S')[0][1])
    end_point = int(np.argwhere(maze == 'E')[0][0]), int(np.argwhere(maze == 'E')[0][1])
    start_direction = (0, 1)
    start_score = 0

    scores = [[[np.inf for _ in range(4)] for x in range(maze.shape[0])] for y in range(maze.shape[1])]
    scores[start_point[0]][start_point[1]][directions.index(start_direction)] = 0

    stack = deque()
    stack.append((start_point, start_direction, start_score, [start_point]))
    paths = []
    best_score = np.inf

    while stack:
        (x, y), direction, score, path = stack.popleft()
        if (x, y) == end_point:
            paths.append(path)
            best_score = score
            continue
        if scores[x][y][directions.index(direction)] < score:
            continue
        scores[x][y][directions.index(direction)] = score

        next_direction_score_list = [(direction, score + 1),
                                     (turn_right(direction), score + 1001),
                                     (turn_left(direction), score + 1001)]
        for next_direction, next_score in next_direction_score_list:
            next_x, next_y = x + next_direction[0], y + next_direction[1]
            if maze[next_x, next_y] != '#' and (next_x, next_y) not in path:
                stack.append(((next_x, next_y), next_direction, next_score, path + [(next_x, next_y)]))

    path_scores = [calc_score(path) for path in paths]
    min_score = min(path_scores)

    print(f'Part 1: {min_score}')

    best_paths = []
    for i in range(len(path_scores)):
        if path_scores[i] == min_score:
            best_paths.append(paths[i])

    best_points = set()
    for path in best_paths:
        for point in path:
            best_points.add(point)

    print(f'Part 2: {len(best_points)}')
