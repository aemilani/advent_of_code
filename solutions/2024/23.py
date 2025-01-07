from collections import defaultdict
from itertools import combinations


def get_graph(input_string: str) -> defaultdict:
    connections = [(row.split('-')[0], row.split('-')[1]) for row in input_string.strip().split('\n')]
    graph = defaultdict(list)
    for c1, c2 in connections:
        graph[c1].append(c2)
        graph[c2].append(c1)
    return graph


def part_1(input_string: str) -> int:
    graph = get_graph(input_string)

    cycles = []
    for c1 in graph:
        for c2 in graph[c1]:
            for c3 in graph[c2]:
                for c4 in graph[c3]:
                    if c4 == c1:
                        if {c1, c2, c3} not in cycles:
                            cycles.append({c1, c2, c3})
                        break

    n = 0
    for c1, c2, c3 in cycles:
        if 't' in [c1[0], c2[0], c3[0]]:
            n += 1
    return n


def part_2(input_string: str) -> str:
    graph = get_graph(input_string)
    c_list = []
    for k, v in graph.items():
        comb = combinations(v, len(v) - 1)
        for v_tup in comb:
            set_list = [set(v_tup) | {k}]
            for c in v_tup:
                set_list.append(set(graph[c]) | {c})
            if len(set.intersection(*set_list)) > 0:
                c_list.append(set.intersection(*set_list))
    lens = [len(s) for s in c_list]
    max_len = max(lens)
    password = ''
    for c in sorted(list(c_list[lens.index(max_len)])):
        password += c
        password += ','
    return password[:-1]


if __name__ == '__main__':
    with open('../../data/input/23.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')

    print(f'Part 2: {part_2(string)}')
