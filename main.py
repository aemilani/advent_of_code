import numpy as np


data = np.loadtxt('simple_input.txt', dtype=str, delimiter=' ')
matrix = []
for l in data:
    matrix.append(list(l))
matrix = np.array(matrix)

plot = np.zeros(shape=matrix.shape)
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 0:
            continue
        letter = matrix[i, j]
        plot[i, j] = 1
        matrix[i, j] = 0
        letter_right = matrix[i, j + 1]
        letter_down = matrix[i + 1, j]
        if letter_right == letter:
            plot[i, j + 1] = 1
            matrix[i, j + 1] = 0
        if letter_down == letter:
            plot[i + 1, j] = 1
            matrix[i + 1, j] = 0