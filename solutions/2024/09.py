import numpy as np


def decode_map(disk_map):
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk.extend(int(disk_map[i]) * [str(i // 2)])
        else:
            disk.extend(int(disk_map[i]) * ['.'])
    return disk


def decode_map_file(disk_map):
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk.append(int(disk_map[i]) * [str(i // 2)])
        else:
            if int(disk_map[i]) != 0:
                disk.append(int(disk_map[i]) * ['.'])
    return disk


def is_refactored(disk):
    dot_indices = [int(s == '.') for s in disk]
    diff = np.array(dot_indices[1:]) - np.array(dot_indices[:-1])
    return np.all(diff >= 0)


def defrag(disk):
    while not is_refactored(disk):
        for i in range(len(disk) - 1, -1, -1):
            if disk[i].isdigit():
                digit = disk[i]
                digit_swapped = False
                for j in range(len(disk)):
                    if disk[j] == '.':
                        disk[i] = '.'
                        disk[j] = digit
                        digit_swapped = True
                        break
                if digit_swapped:
                    break
    return disk


def defrag_file(disk_file):
    i = -1
    while i > -len(disk_file):
        if disk_file[i][0].isdigit():
            digit_list = disk_file[i]
            digit_len = len(digit_list)
            for j in range(len(disk_file) + i):
                if disk_file[j][0] == '.' and len(disk_file[j]) >= digit_len:
                    space_len = len(disk_file[j])
                    disk_file[i] = ['.'] * len(digit_list)
                    disk_file[j] = digit_list
                    if space_len > digit_len:
                        disk_file.insert(j + 1, ['.'] * (space_len - digit_len))
                    break
        i -= 1
    return disk_file


def checksum(disk):
    res = 0
    for i, s in enumerate(disk):
        if s.isdigit():
            res += i * int(s)
    return res


if __name__ == "__main__":
    with open('../../data/input/09.txt', 'r') as f:
        string = f.read().strip()

    disk = decode_map(string)
    print(f'Part 1: {checksum(defrag(disk))}')

    disk_file = decode_map_file(string)

    defraged_file_list = defrag_file(disk_file)
    defraged_file = []
    for lis in defraged_file_list:
        defraged_file.extend(lis)

    print(f'Part 2: {checksum(defraged_file)}')
