import numpy as np


def do_operation(n1, n2, op):
    if op == '0':
        return n1 + n2
    elif op == '1':
        return n1 * n2
    elif op == '2':
        return int(str(n1) + str(n2))


if __name__ == "__main__":
    with open('../../data/2024/07.txt', 'r') as f:
        string = f.read().strip()
    lis = string.split('\n')

    sum_true_values = 0
    for line in lis:
        value = int(line.split(':')[0])
        numbers = [int(number) for number in line.split(':')[1].strip().split(' ')]
        # numbers = line.split(':')[1].strip().split(' ')
        n_operators = 2  # + and *
        n_spaces = len(numbers) - 1
        n_operator_combinations = n_operators ** n_spaces

        for i in range(n_operator_combinations):
            operators = bin(i)[2:].zfill(n_spaces)
            result = numbers[0]
            for operator, n2 in zip(operators, numbers[1:]):
                result = do_operation(result, n2, operator)
            if result == value:
                sum_true_values += value
                break

    print(f'Part 1: {sum_true_values}')

    sum_true_values = 0
    for ct, line in enumerate(lis):
        print(f'{ct} / {len(lis)}')
        value = int(line.split(':')[0])
        numbers = [int(number) for number in line.split(':')[1].strip().split(' ')]
        n_operators = 3  # + and * and ||
        n_spaces = len(numbers) - 1
        n_operator_combinations = n_operators ** n_spaces

        for i in range(n_operator_combinations):
            operators = np.base_repr(i, base=n_operators).zfill(n_spaces)
            result = numbers[0]
            for operator, n2 in zip(operators, numbers[1:]):
                result = do_operation(result, n2, operator)
            if result == value:
                sum_true_values += value
                break

    print(f'Part 2: {sum_true_values}')
