from itertools import permutations
from typing import Set, Tuple, List, Dict
from functools import cache


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

num_loc = {'A': (3, 2),
           '0': (3, 1),
           '1': (2, 0),
           '2': (2, 1),
           '3': (2, 2),
           '4': (1, 0),
           '5': (1, 1),
           '6': (1, 2),
           '7': (0, 0),
           '8': (0, 1),
           '9': (0, 2)}

dir_loc = {'A': (0, 2),
           '^': (0, 1),
           '<': (1, 0),
           'v': (1, 1),
           '>': (1, 2)}

direction_dic = {'>': (0, 1),
                 'v': (1, 0),
                 '<': (0, -1),
                 '^': (-1, 0)}


def create_graph(loc_dict: Dict[str, Tuple[int, int]], invalid_coords: Tuple[int, int]) -> Dict[Tuple[str, str], str]:
    graph = {}
    for a, (x1, y1) in loc_dict.items():
        for b, (x2, y2) in loc_dict.items():
            path = '<' * (y1 - y2) + 'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
            if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                path = path[::-1]
            graph[(a, b)] = path + 'A'
    return graph


def convert(sequence: str, graph: Dict[Tuple[str, str], str]) -> str:
    conversion = ''
    prev = 'A'
    for char in sequence:
        conversion += graph[(prev, char)]
        prev = char
    return conversion


def part_1(input_string: str) -> int:
    num_graph = create_graph(num_loc, (3, 0))
    dir_graph = create_graph(dir_loc, (0, 0))

    complexity = 0
    for code in input_string.split('\n'):
        conversion = convert(code, num_graph)
        conversion = convert(conversion, dir_graph)
        conversion = convert(conversion, dir_graph)
        complexity += int(code[:-1]) * len(conversion)

    return complexity


def part_2(input_string: str) -> int:
    num_graph = create_graph(num_loc, (3, 0))
    dir_graph = create_graph(dir_loc, (0, 0))

    @cache
    def get_length(sequence: str, iterations: int) -> int:
        if iterations == 0:
            return len(sequence)
        prev = 'A'
        total_length = 0
        for char in sequence:
            total_length += get_length(dir_graph[(prev, char)], iterations - 1)
            prev = char
        return total_length

    complexity = 0
    for code in input_string.split('\n'):
        conversion = convert(code, num_graph)
        final_len = get_length(conversion, 25)
        complexity += int(code[:-1]) * final_len

    return complexity


if __name__ == '__main__':
    with open('../../data/input/21.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')

    print(f'Part 2: {part_2(string)}')
