from collections import deque
from itertools import permutations
from typing import Set, Tuple, List


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
    moves = []
    for c in command:
        new_loc = dir_loc[c]
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
                if (x, y) == (0, 0):
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


if __name__ == '__main__':
    with open('../../data/input/21.txt', 'r') as f:
        string = f.read().strip()

    codes = string.split('\n')

    complexity = 0
    for code in codes:
        out_1 = numeric_to_directional(code)
        out_2 = []
        for out in out_1:
            out_2.extend(directional_to_directional(out))
        out_3 = []
        for out in out_2:
            out_3.extend(directional_to_directional(out))
        min_len = min([len(s) for s in out_3])
        min_len_out = [s for s in out_3 if len(s) == min_len]
        complexity += min_len * int(code[:-1])

    print(f'Part 1: {complexity}')
