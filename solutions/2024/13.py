import numpy as np
from typing import List, Tuple


def calc_cost(a_times: int, b_times: int) -> int:
    """Calculate the cost of button presses."""
    return a_times * 3 + b_times


def find_button_combination(a_move: Tuple[int, int], b_move: Tuple[int, int],
                            prize: Tuple[int, int]) -> Tuple[int, int] | None:
    """Find the only button combination. (There is only one!)"""
    a = (b_move[0] * prize[1] - b_move[1] * prize[0]) // (a_move[1] * b_move[0] - a_move[0] * b_move[1])
    a_res = (b_move[0] * prize[1] - b_move[1] * prize[0]) % (a_move[1] * b_move[0] - a_move[0] * b_move[1])
    b = (prize[0] - a * a_move[0]) // b_move[0]
    b_res = (prize[0] - a * a_move[0]) % b_move[0]
    if a_res == 0 and b_res == 0:
        return a, b
    else:
        return None


def decode_input_string(string_input: str) -> List[List[Tuple[int, int]]]:
    machines = []
    for entry in string_input.split('\n\n'):
        machine_str = [op.split(':')[1].strip() for op in entry.split('\n')]
        machine_list = []
        for i in range(len(machine_str)):
            tup = ()
            for ax in machine_str[i].split(','):
                if i < 2:
                    tup += (int(ax.split('+')[1]),)
                else:
                    tup += (int(ax.split('=')[1]),)
            machine_list.append(tup)
        machines.append(machine_list)
    return machines


if __name__ == "__main__":
    with open('../../data/input/13.txt', 'r') as f:
        string = f.read().strip()

    claw_machines = decode_input_string(string)

    cost = 0
    for machine in claw_machines:
        comb = find_button_combination(machine[0], machine[1], machine[2])
        if comb:
            cost += calc_cost(comb[0], comb[1])

    print(f'Part 1: {cost}')

    cost = 0
    for machine in claw_machines:
        addition = 10000000000000
        comb = find_button_combination(machine[0], machine[1], (machine[2][0] + addition, machine[2][1] + addition))
        if comb:
            cost += calc_cost(comb[0], comb[1])

    print(f'Part 2: {cost}')
