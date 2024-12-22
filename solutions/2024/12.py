import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def plot_edges(edges):
    """
    Plots the shape formed by a list of edge coordinates with (0, 0) at the top-left.

    Parameters:
    edges (list of tuples): List of edges in the form [[(x1, y1), (x2, y2)], ...]
    """
    for edge in edges:
        x_coords, y_coords = zip(*edge)  # Unzip the points of the edge
        plt.plot(x_coords, y_coords, 'bo-', linewidth=2)  # Plot the edge with blue points and lines

    # Adjust the plot for better visualization
    plt.gca().invert_yaxis()  # Invert the Y-axis
    plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis (inverted)')
    plt.title('Shape Formed by Edges')
    plt.grid(True)
    plt.show()


def is_valid_move(x, y, prev_value, matrix):
    """Check if a move is valid."""
    return 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1] and matrix[x, y] == prev_value


def dfs(x, y, region, visited, matrix, directions, borders):
    visited.add((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, matrix[x, y], matrix):
            if (nx, ny) not in visited:
                region.append((nx, ny))
                dfs(nx, ny, region, visited, matrix, directions, borders)
        else:
            # x, y are assumed to be the top left coordinates of each square
            if dx == 0:
                if dy == 1:
                    borders.append([(nx, ny), (nx + 1, ny)])
                elif dy == -1:
                    borders.append([(nx, ny + 1), (nx + 1, ny + 1)])
            elif dy == 0:
                if dx == 1:
                    borders.append([(nx, ny), (nx, ny + 1)])
                elif dx == -1:
                    borders.append([(nx + 1, ny), (nx + 1, ny + 1)])


def step_border(border: List[Tuple[int, int]], all_borders: List[List[Tuple[int, int]]], path: List[Tuple[int, int]]):
    point = [p for p in border if p != path[-1]][0]
    path.append(point)
    all_borders.remove(border)
    if point == path[0]:
        return
    neighbours = [b for b in all_borders if point in b]
    if len(neighbours) == 1:
        step_border(neighbours[0], all_borders, path)
    elif len(neighbours) > 1:
        orthogonal_neighbours = [b for b in all_borders if b != border and point in b
                                 and (b[0][0] - b[1][0]) != (border[0][0] - border[1][0])]
        neighbour = orthogonal_neighbours[0]
        step_border(neighbour, all_borders, path)


def calc_sides(path: List[Tuple[int, int]]):
    diffs = [p[0] - q[0] for p, q in zip(path[1:], path[:-1])]
    n_sides = 1
    for i in range(1, len(diffs)):
        if diffs[i] != diffs[i - 1]:
            n_sides += 1
    return n_sides


def run(plots: str) -> Tuple[int, int]:
    mat = np.array([list(line) for line in plots.split('\n')])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited = set()
    cost = 0
    cost_discount = 0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if (i, j) not in visited:
                borders = []
                region = [(i, j)]
                dfs(i, j, region, visited, mat, directions, borders)
                area = len(region)
                perimeter = len(borders)
                borders = sorted(borders)

                n_sides = 0
                while len(borders) > 0:
                    path = [borders[0][0]]
                    step_border(borders[0], borders, path)
                    n_sides += calc_sides(path)

                cost += area * perimeter
                cost_discount += area * n_sides
    return cost, cost_discount


def test_run():
    plots_list = ['AAAA\nBBCD\nBBCC\nEEEC', 'OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO', 'EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE',
                  'AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA',
                  'RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\n'
                  'MIIISIJEEE\nMMMISSJEEE',
                  'AAAEAAAAAA\nFFAEAADAAA\nFFAAAADACA\nFFAABAAAAB\nFFABBBABBB\nFAAAABBBBB\nFAGGABBBBB\nFAGAABBBBB',
                  'LDDDDDDXXX\nLLLDDVDXXX\nLLLDDDXXXX', 'BBBBBC\nBAAABC\nBABABC\nBAABBB\nBABABC\nBAAABC',
                  'AAAAA\nABABA\nABBBA\nABABA', '----\n-OOO\n-O-O\nOO-O\n-OOO',
                  'VVVVVCRRCCCCCCCYYC\nCVCCVCCCCCCCCCCYCC\nCCCCCCCCCCCCCCCCCC\nCCCQQCCCCCCCCCCCCC\nQQQQCCCCCCCCCCCCCC\n'
                  'QQQQQQCCCCCCCCCCCC\nQQQQQQQCCKCKKCCCYY\nQQQQQQQQKKKKKKKCYY']
    cost_2_list = [80, 436, 236, 368, 1206, 1992, 250, 492, 232, 180, 4614]
    for plots, cost_2_true in zip(plots_list, cost_2_list):
        _, cost_2_answer = run(plots)
        assert cost_2_answer == cost_2_true
    print('Test passed.')
    

if __name__ == "__main__":
    test_run()

    with open('../../data/input/12.txt', 'r') as f:
        string = f.read().strip()

    cost_1, cost_2 = run(string)

    print(f'Part 1: {cost_1}')
    print(f'Part 2: {cost_2}')
