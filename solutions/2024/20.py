from typing import List, Tuple
from collections import deque
from copy import deepcopy

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def set_shortest_path_lens(maze: List[List[str]], end: Tuple[int, int]) -> List[List[str | int]]:
    maze_cpy = deepcopy(maze)
    maze_cpy[end[0]][end[1]] = 0

    stack = deque()
    stack.append((end, 0))
    while stack:
        (x, y), score = stack.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze_cpy) and 0 <= ny < len(maze_cpy[0]) and
                    (maze_cpy[nx][ny] == '.' or (isinstance(maze_cpy[nx][ny], int) and maze_cpy[nx][ny] > score))):
                maze_cpy[nx][ny] = score + 1
                stack.append(((nx, ny), score + 1))
    return maze_cpy


if __name__ == '__main__':
    with open('../../data/input/20.txt', 'r') as f:
        string = f.read().strip()

    # string = '..............................................\n....####################################......\n....#.................................E#......\n....#.##################################......\n....#.#.......................................\n....#.##################################......\n....#..................................#......\n....##################################.#......\n.....................................#.#......\n....##################################.#......\n....#..................................#......\n....#.##################################......\n....#.#.......................................\n....#.##################################......\n....#.................................S#......\n....####################################......\n..............................................'

    maze = [list(row) for row in string.split('\n')]
    start_point, end_point = None, None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start_point = (i, j)
            elif maze[i][j] == 'E':
                end_point = (i, j)
    maze[start_point[0]][start_point[1]] = '.'
    maze[end_point[0]][end_point[1]] = '.'

    maze_path = set_shortest_path_lens(maze, end_point)

    shortest_path = [start_point]
    score = maze_path[start_point[0]][start_point[1]]
    while score != 0:
        for dx, dy in directions:
            nx, ny = shortest_path[-1][0] + dx, shortest_path[-1][1] + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and \
                    maze_path[nx][ny] == (score - 1):
                shortest_path.append((nx, ny))
                score = maze_path[nx][ny]

    cheats = 0
    for x, y in shortest_path:
        time = maze_path[x][y]
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                    isinstance(maze_path[nx][ny], int) and (maze_path[nx][ny] - time) >= 102):
                cheats += 1

    print(f'Part 1: {cheats}')

    cheats = 0
    for t1 in range(len(shortest_path) - 100):
        for t2 in range(t1, len(shortest_path)):
            x1, y1 = shortest_path[t1]
            x2, y2 = shortest_path[t2]
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= 20 and t2 - t1 - distance >= 100:
                cheats += 1

    print(f'Part 2: {cheats}')
