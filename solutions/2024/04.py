import numpy as np


with open('../../data/input/04.txt', 'r') as f:
    string = f.read().strip()

mat = []
for s in string.split():
    mat.append(list(s))
mat = np.array(mat)

ct = 0
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        try:
            if list(mat[i, j:j + 4]) == ['X', 'M', 'A', 'S']:
                ct += 1
        except IndexError:
            pass
        try:
            if list(mat[i, j - 3:j + 1]) == ['S', 'A', 'M', 'X'] and j >= 3:
                ct += 1
        except IndexError:
            pass
        try:
            if list(mat[i:i + 4, j]) == ['X', 'M', 'A', 'S']:
                ct += 1
        except IndexError:
            pass
        try:
            if list(mat[i - 3:i + 1, j]) == ['S', 'A', 'M', 'X'] and i >= 3:
                ct += 1
        except IndexError:
            pass
        try:
            if [mat[i, j], mat[i + 1, j + 1], mat[i + 2, j + 2], mat[i + 3, j + 3]] == ['X', 'M', 'A', 'S']:
                ct += 1
        except IndexError:
            pass
        try:
            if [mat[i, j], mat[i + 1, j - 1], mat[i + 2, j - 2], mat[i + 3, j - 3]] == ['X', 'M', 'A', 'S'] and j >= 3:
                ct += 1
        except IndexError:
            pass
        try:
            if [mat[i, j], mat[i - 1, j + 1], mat[i - 2, j + 2], mat[i - 3, j + 3]] == ['X', 'M', 'A', 'S'] and i >= 3:
                ct += 1
        except IndexError:
            pass
        try:
            if [mat[i, j], mat[i - 1, j - 1], mat[i - 2, j - 2], mat[i - 3, j - 3]] == ['X', 'M', 'A', 'S'] and\
                    i >= 3 and j >= 3:
                ct += 1
        except IndexError:
            pass

print(f'Part 1: {ct}')

ct = 0
for i in range(1, mat.shape[0] - 1):
    for j in range(1, mat.shape[1] - 1):
        try:
            if mat[i, j] == 'A' and ((mat[i + 1, j + 1] == 'S' and mat[i - 1, j - 1] == 'M') or
                                     (mat[i + 1, j + 1] == 'M' and mat[i - 1, j - 1] == 'S')) and\
                    ((mat[i + 1, j - 1] == 'S' and mat[i - 1, j + 1] == 'M') or
                     (mat[i + 1, j - 1] == 'M' and mat[i - 1, j + 1] == 'S')):
                ct += 1
        except IndexError:
            pass
print(f'Part 2: {ct}')
