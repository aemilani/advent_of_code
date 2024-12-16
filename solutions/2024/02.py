import numpy as np


def is_safe(arr):
    arr_diff = arr[1:] - arr[:-1]
    if np.all((arr_diff >= 1) & (arr_diff <= 3)) or np.all((arr_diff <= -1) & (arr_diff >= -3)):
        return True
    else:
        return False


def is_safe_tol(arr):
    if is_safe(arr):
        return True
    else:
        for i in range(len(arr)):
            if is_safe(np.delete(arr, i)):
                return True
    return False


if __name__ == "__main__":
    with open('../../data/input/02.txt', 'r') as f:
        string = f.read().strip()
    reports = string.split('\n')

    # reports = ['7 6 4 2 1', '1 2 5 8 9', '9 7 6 8 1', '9 7 6 8 5', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 6 6']

    n_safe = 0
    for report in reports:
        arr = np.array(report.split(), dtype=int)
        if is_safe(arr):
            n_safe += 1
    print(f'Part 1: {n_safe}')

    n_safe_tol = 0
    for report in reports:
        arr = np.array(report.split(), dtype=int)
        if is_safe_tol(arr):
            n_safe_tol += 1
    print(f'Part 2: {n_safe_tol}')
