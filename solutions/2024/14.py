import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def decode_input_string(string_input: str) -> List[List[Tuple[int, int]]]:
    robots = []
    for robot in string_input.split('\n'):
        p, v = robot.split(' ')
        p = p.split('=')[1].split(',')
        v = v.split('=')[1].split(',')
        robots.append([(int(p[0]), int(p[1])), (int(v[0]), int(v[1]))])
    return robots


def step_robot(loc: Tuple[int, int], vel: Tuple[int, int], map_size: Tuple[int, int] = (101, 103)) -> Tuple[int, int]:
    x = loc[0] + vel[0]
    if x >= map_size[0]:
        x = x % map_size[0]
    elif x < 0:
        x = map_size[0] - abs(x) % map_size[0]

    y = loc[1] + vel[1]
    if y >= map_size[1]:
        y = y % map_size[1]
    elif y < 0:
        y = map_size[1] - abs(y) % map_size[1]

    return x, y


def step_robots(robots: List[List[Tuple[int, int]]],
                map_size: Tuple[int, int] = (101, 103)) -> List[List[Tuple[int, int]]]:
    robots_updated = []
    for p, v in robots:
        robots_updated.append([step_robot(p, v, map_size), v])
    return robots_updated


def get_grid(robots: List[List[Tuple[int, int]]], map_size: Tuple[int, int] = (101, 103)) -> np.array:
    grid = np.zeros((map_size[1], map_size[0]))
    for p, _ in robots:
        grid[p[1], p[0]] += 1
    return grid


def run(robots: List[List[Tuple[int, int]]], steps: int, map_size: Tuple[int, int] = (101, 103)) -> np.array:
    for _ in range(steps):
        robots = step_robots(robots, map_size)
    final_grid = get_grid(robots, map_size)
    return final_grid


def calc_safety_factor(grid: np.array) -> int:
    y, x = grid.shape
    quadrants = []
    for yi, yj in zip([0, y // 2 + 1], [y // 2, y]):
        for xi, xj in zip([0, x // 2 + 1], [x // 2, x]):
            quadrants.append(grid[yi:yj, xi:xj])
    safety_factor = 1
    for quad in quadrants:
        safety_factor *= quad.sum()
    return safety_factor


if __name__ == "__main__":
    with open('../../data/2024/14.txt', 'r') as f:
        string = f.read().strip()

    robot_list = decode_input_string(string)
    grid = run(robot_list, 100)

    safety_factor = calc_safety_factor(grid)

    print(f'Part 1: {safety_factor}')

    robot_list = decode_input_string(string)

    safety_factors = []
    for i in range(1, 10000):
        robot_list = step_robots(robot_list)
        safety_factors.append(calc_safety_factor(get_grid(robot_list)))

    min_safety_factor_index = int(np.argmin(safety_factors)) + 1

    print(f'Part 2: {min_safety_factor_index}')

    robot_list = decode_input_string(string)
    grid = run(robot_list, min_safety_factor_index)

    plt.figure()
    plt.imshow(grid)
    plt.show()
