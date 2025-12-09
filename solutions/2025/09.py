from typing import Tuple, List


def area(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def get_polygon_edges(points: List[tuple[int, int]]) -> List[tuple[tuple[int, int], tuple[int, int]]]:
    edges = []
    n = len(points)
    for i in range(n):
        edges.append((points[i], points[(i + 1) % n]))
    return edges


def is_point_in_polygon(x: float, y: float, edges: List) -> bool:
    """
    Ray Casting Algorithm to check if a point (x,y) is inside the polygon.
    We shoot a ray from (x,y) to (infinity, y) and count intersections.
    Odd intersections = Inside. Even = Outside.
    """
    inside = False
    for (x1, y1), (x2, y2) in edges:
        # Check if the edge intersects the horizontal ray to the right of x
        # We check if y is between y1 and y2
        if min(y1, y2) < y < max(y1, y2):
            # Calculate x-coordinate of intersection
            # x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            # Since edges are strictly vertical or horizontal in this problem:
            if x1 == x2:  # Vertical edge
                if x1 > x:
                    inside = not inside
            else:  # Horizontal edge
                # A horizontal edge cannot be crossed by a horizontal ray strictly
                # inside it (we use floating point midpoints to avoid collinearity)
                pass

    return inside


def rect_intersects_edge(rx_min, rx_max, ry_min, ry_max, edge) -> bool:
    """
    Checks if a polygon edge strictly passes through the INTERIOR of the rectangle.
    Edges lying ON the rectangle boundary are permitted (and return False here).
    """
    (x1, y1), (x2, y2) = edge

    # 1. Check Vertical Edge
    if x1 == x2:
        # Edge X must be strictly inside Rect X bounds
        if rx_min < x1 < rx_max:
            # Edge Y interval and Rect Y interval must strictly overlap
            overlap_min = max(ry_min, min(y1, y2))
            overlap_max = min(ry_max, max(y1, y2))
            if overlap_min < overlap_max:
                return True

    # 2. Check Horizontal Edge
    elif y1 == y2:
        # Edge Y must be strictly inside Rect Y bounds
        if ry_min < y1 < ry_max:
            # Edge X interval and Rect X interval must strictly overlap
            overlap_min = max(rx_min, min(x1, x2))
            overlap_max = min(rx_max, max(x1, x2))
            if overlap_min < overlap_max:
                return True

    return False


def part_1(input_string: str) -> int:
    points = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in input_string.split('\n')]
    areas = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            areas.append(area(points[i], points[j]))
    return max(areas)


def part_2(input_string: str) -> int:
    points = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in input_string.split('\n')]
    edges = get_polygon_edges(points)
    n = len(points)
    max_area = 0

    # Iterate through all pairs of red tiles
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            # Define current rectangle bounds
            min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
            min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

            # Calculate Area
            current_area = (max_x - min_x + 1) * (max_y - min_y + 1)

            # Optimization: Don't check validity if this area is smaller than best found
            if current_area <= max_area:
                continue

            # Check 1: Does any polygon edge cut through the interior?
            intersecting = False
            for edge in edges:
                if rect_intersects_edge(min_x, max_x, min_y, max_y, edge):
                    intersecting = True
                    break
            if intersecting:
                continue

            # Check 2: Is the center of the rectangle actually inside the polygon?
            # We use a slight offset to ensure we don't hit integer boundaries with Ray Casting
            mid_x = (min_x + max_x) / 2
            mid_y = (min_y + max_y) / 2

            if is_point_in_polygon(mid_x + 0.001, mid_y + 0.001, edges):
                max_area = current_area

    return max_area


if __name__ == '__main__':
    with open('../../data/2025/09.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
