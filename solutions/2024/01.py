import numpy as np


with open('../../data/input/01.txt', 'r') as f:
    string = f.read().strip()

l1 = np.sort(np.array(string.split()[:-1:2]).astype(int))
l2 = np.sort(np.array(string.split()[1::2]).astype(int))

print(f'Part 1: {np.sum(np.abs(l1 - l2))}')

similarity_score = 0
for elem in l1:
    similarity_score += np.count_nonzero((l2 == elem).astype(int)) * elem

print(f'Part 2: {similarity_score}')
