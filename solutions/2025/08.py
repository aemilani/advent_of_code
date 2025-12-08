from typing import Tuple
from collections import defaultdict
from math import prod


def distance(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> int:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5


def find_connected_components(edges, all_nodes=None):
    # 1. Build the graph (Adjacency List)
    graph = defaultdict(set)
    nodes_in_edges = set()

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        nodes_in_edges.add(u)
        nodes_in_edges.add(v)

    # 2. Add isolated nodes to the graph
    # If a master list of nodes is provided, add any that weren't in the edges
    if all_nodes:
        for node in all_nodes:
            if node not in nodes_in_edges:
                # Add to graph with an empty set of neighbors
                graph[node] = set()

    visited = set()
    components = []

    # 3. Iterate through ALL nodes in the graph
    for node in graph:
        if node not in visited:
            component = []
            stack = [node]
            visited.add(node)

            while stack:
                current_node = stack.pop()
                component.append(current_node)

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            components.append(tuple(sorted(component)))

    return components


def part_1(input_string: str, n_connections: int) -> int:
    points = [(int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2]))
                   for line in input_string.split('\n')]

    pairs = []  # Store as (dist, index_1, index_2)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            pairs.append((d, i, j))

    pairs.sort(key=lambda x: x[0])
    edges = [(p[1], p[2]) for p in pairs[:n_connections]]
    circuits = find_connected_components(edges)
    longest = sorted([len(c) for c in circuits], reverse=True)[:3]
    return prod(longest)


def part_2(input_string: str) -> int | None:
    points = [(int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2]))
                   for line in input_string.split('\n')]

    pairs = []  # Store as (dist, index_1, index_2)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            pairs.append((d, i, j))

    pairs.sort(key=lambda x: x[0])
    for n_connections in range(len(pairs)):
        edges = [(p[1], p[2]) for p in pairs[:n_connections]]
        circuits = find_connected_components(edges, range(len(points)))
        if len(circuits) == 1:
            p1 = pairs[n_connections - 1][1]
            p2 = pairs[n_connections - 1][2]
            return points[p1][0] * points[p2][0]

    return None


if __name__ == '__main__':
    with open('../../data/2025/08.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string, 1000)}')
    print(f'Part 2: {part_2(string)}')
