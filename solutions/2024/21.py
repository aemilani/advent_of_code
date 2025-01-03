from itertools import permutations
from typing import Set, Tuple, List
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


def permute(l1: List[str], l2: List[str]) -> List[str]:
    combinations = []
    for s1 in l1:
        for s2 in l2:
            combinations.append(s1 + 'A' + s2)
    return combinations


def numeric_to_directional(command):
    loc = num_loc['A']
    moves = []
    for c in command:
        new_loc = num_loc[c]
        dx, dy = new_loc[0] - loc[0], new_loc[1] - loc[1]

        move = []
        if dx > 0:
            for _ in range(dx):
                move.append('v')
        else:
            for _ in range(-dx):
                move.append('^')
        if dy > 0:
            for _ in range(dy):
                move.append('>')
        else:
            for _ in range(-dy):
                move.append('<')
        move_permutations = set(permutations(move))

        correct_perms: List[str] = []
        for perm in move_permutations:
            x, y = loc
            correct_perm = True
            for c in perm:
                x += direction_dic[c][0]
                y += direction_dic[c][1]
                if (x, y) == (3, 0):
                    correct_perm = False
            if correct_perm:
                correct_perms.append(''.join(perm))
        moves.append(correct_perms)
        loc = new_loc

    output = ['']
    for move in moves:
        output = permute(output, move)
    for i in range(len(output)):
        output[i] = output[i][1:] + 'A'

    return output


def directional_to_directional(command):
    loc = dir_loc['A']
    output = ''
    for c in command:
        new_loc = dir_loc[c]
        move = char_to_directional(loc, new_loc)
        output += move
        output += 'A'
        loc = new_loc
    return output


@cache
def char_to_directional(loc, new_loc):
    dx, dy = new_loc[0] - loc[0], new_loc[1] - loc[1]
    if dx > 0:
        x_move = 'v'
    else:
        x_move = '^'
    if dy > 0:
        y_move = '>'
    else:
        y_move = '<'

    move = ''
    if dx == 0 and dy != 0:
        for _ in range(abs(dy)):
            move += y_move
    elif dy == 0 and dx != 0:
        for _ in range(abs(dx)):
            move += x_move
    elif dx != 0 and dy != 0:
        if (abs(loc[0] - dir_loc[x_move][0]) + abs(loc[1] - dir_loc[x_move][1])) < \
                (abs(loc[0] - dir_loc[y_move][0]) + abs(loc[1] - dir_loc[y_move][1])):
            for _ in range(abs(dx)):
                move += x_move
            for _ in range(abs(dy)):
                move += y_move
        else:
            for _ in range(abs(dy)):
                move += y_move
            for _ in range(abs(dx)):
                move += x_move
    return move


def part_1(input_str):
    codes = input_str.split('\n')

    complexity = 0
    for code in codes:
        out_1 = numeric_to_directional(code)
        out_2 = []
        for out in out_1:
            out_2.append(directional_to_directional(out))
        out_3 = []
        for out in out_2:
            out_3.append(directional_to_directional(out))
        min_len = min([len(s) for s in out_3])
        complexity += min_len * int(code[:-1])
    return complexity


def part_2(input_str):
    codes = input_str.split('\n')

    complexity = 0
    for code in codes:
        out_1 = numeric_to_directional(code)
        out_2 = []
        for out in out_1:
            for i in range(25):
                print(f'{i + 1} / {25}')
                out = directional_to_directional(out)
            out_2.append(out)
        min_len = min([len(s) for s in out_2])
        complexity += min_len * int(code[:-1])

    return complexity


if __name__ == '__main__':
    with open('../../data/input/21.txt', 'r') as f:
        string = f.read().strip()

    print(f'Part 1: {part_1(string)}')

    print(f'Part 2: {part_2(string)}')
