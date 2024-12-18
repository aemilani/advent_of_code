import numpy as np


# with open('../../data/input/10.txt', 'r') as f:
#     string = f.read().strip()

string = '89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732'
mat = np.array([list(line) for line in string.split('\n')]).astype(int)

print(mat)
zero_inds = [(int(coord[0]), int(coord[1])) for coord in list(np.argwhere(mat == 0))]
print(zero_inds)
