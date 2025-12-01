def part_1(input_string: str) -> int:
    l = input_string.split('\n')
    curr = 50

    zeros = 0
    for op in l:
        if op[0] == 'L':
            dist = -int(op[1:])
        else:
            dist = int(op[1:])
        curr += dist
        curr = curr % 100

        if curr == 0:
            zeros += 1

    return zeros


def hits_on_zero_in_rotation(old: int, steps: int, direction: str) -> int:
    """
    Count how many times the dial hits 0 during a rotation of `steps` clicks
    starting from `old` (0..99). direction is 'L' or 'R'.
    """
    if steps <= 0:
        return 0

    if direction == 'R':
        k0 = (100 - old) % 100
    else:  # 'L'
        k0 = old % 100

    # If k0 == 0 that means you'd hit 0 after 100 clicks (not 0 clicks)
    if k0 == 0:
        k0 = 100

    if steps < k0:
        return 0
    else:
        return 1 + (steps - k0) // 100


def part_2(input_string: str) -> int:
    lines = [ln for ln in input_string.splitlines() if ln.strip() != ""]
    curr = 50
    zeros = 0
    for op in lines:
        direction = op[0]
        steps = int(op[1:])
        zeros += hits_on_zero_in_rotation(curr, steps, direction)

        # update current position (circular 0..99)
        if direction == 'L':
            curr = (curr - steps) % 100
        else:
            curr = (curr + steps) % 100

    return zeros


if __name__ == '__main__':
    with open('../../data/2025/01.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')
    print(f'Part 2: {part_2(string)}')
