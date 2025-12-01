import numpy as np


with open('../../data/2024/08.txt', 'r') as f:
    string = f.read().strip()
lis = string.split('\n')
mat = np.array([list(elem) for elem in lis])

chars = np.unique(mat)
antenna_types = np.delete(chars, np.argwhere(chars == '.')[0][0])

anti_coords = []
for antenna in antenna_types:
    coords = [(int(coord[0]), int(coord[1])) for coord in list(np.argwhere(mat == antenna))]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            c1, c2 = coords[i], coords[j]
            diff = (c2[0] - c1[0], c2[1] - c1[1])

            anti_coord = (c2[0] + diff[0], c2[1] + diff[1])
            if 0 <= anti_coord[0] < mat.shape[0] and 0 <= anti_coord[1] < mat.shape[1]:
                anti_coords.append(anti_coord)

            anti_coord = (c1[0] - diff[0], c1[1] - diff[1])
            if 0 <= anti_coord[0] < mat.shape[0] and 0 <= anti_coord[1] < mat.shape[1]:
                anti_coords.append(anti_coord)

anti_coords = set(anti_coords)
print(f'Part 1: {len(anti_coords)}')

anti_coords = []
for antenna in antenna_types:
    coords = [(int(coord[0]), int(coord[1])) for coord in list(np.argwhere(mat == antenna))]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            c1, c2 = coords[i], coords[j]
            diff = (c2[0] - c1[0], c2[1] - c1[1])

            mul = 0
            anti_coord = (c2[0] + diff[0] * mul, c2[1] + diff[1] * mul)
            anti_coords.append(anti_coord)
            while True:
                mul += 1
                anti_coord = (c2[0] + diff[0] * mul, c2[1] + diff[1] * mul)
                if 0 <= anti_coord[0] < mat.shape[0] and 0 <= anti_coord[1] < mat.shape[1]:
                    anti_coords.append(anti_coord)
                else:
                    break

            mul = 0
            anti_coord = (c1[0] - diff[0] * mul, c1[1] - diff[1] * mul)
            anti_coords.append(anti_coord)
            while True:
                mul += 1
                anti_coord = (c1[0] - diff[0] * mul, c1[1] - diff[1] * mul)
                if 0 <= anti_coord[0] < mat.shape[0] and 0 <= anti_coord[1] < mat.shape[1]:
                    anti_coords.append(anti_coord)
                else:
                    break

anti_coords = set(anti_coords)
print(f'Part 2: {len(anti_coords)}')
