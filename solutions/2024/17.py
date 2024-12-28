from typing import List, Tuple
from collections import deque

a = None
b = None
c = None


def literal(operand):
    return operand


def combo(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c


def run(program: List[int]):
    global a, b, c
    output = tuple()
    i = 0
    while i < len(program) - 1:
        opcode = program[i]
        operand = program[i + 1]

        if opcode == 0:  # adv
            a = a // 2 ** combo(operand)
        elif opcode == 1:  # bxl
            b = b ^ literal(operand)
        elif opcode == 2:  # bst
            b = combo(operand) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                i = literal(operand)
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            output += (combo(operand) % 8,)
        elif opcode == 6:  # bdv
            b = a // 2 ** combo(operand)
        elif opcode == 7:  # cdv
            c = a // 2 ** combo(operand)

        if opcode != 3 or a == 0:
            i += 2

    return output


def test():
    global a, b, c

    c = 9
    program = [2, 6]
    run(program)
    assert b == 1

    a = 10
    program = [5, 0, 5, 1, 5, 4]
    output = run(program)
    assert output == (0, 1, 2)

    a = 2024
    program = [0, 1, 5, 4, 3, 0]
    output = run(program)
    assert output == (4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0)
    assert a == 0

    b = 29
    program = [1, 7]
    run(program)
    assert b == 26

    b = 2024
    c = 43690
    program = [4, 0]
    run(program)
    assert b == 44354

    print('Passed!')


if __name__ == "__main__":
    with open('../../data/input/17.txt', 'r') as f:
        string = f.read().strip()

    registers = string.split('\n\n')[0].split('\n')
    a = int(registers[0].split(': ')[1])
    b = int(registers[1].split(': ')[1])
    c = int(registers[2].split(': ')[1])

    program_str = string.split('\n\n')[1].split(': ')[1]

    program_list = []
    for elem in program_str.split(','):
        program_list.append(int(elem))

    output_tuple = run(program_list)
    output_str = ''
    for elem in output_tuple:
        output_str += str(elem)
        output_str += ','
    output_str = output_str[:-1]

    print(f'Part 1: {output_str}')

    # The program's output does not depend on b and c
    # The last (opcode, operand) pair of the program only performs recursion to the beginning

    non_recursive_program_list = program_list[:-2]

    a_list = [0]
    for elem in program_list[::-1]:
        previous_a = []
        for a in a_list:
            for i in range(8 * a, 8 * a + 8):
                a = i
                out = run(non_recursive_program_list)[0]
                if elem == out:
                    previous_a.append(i)
        a_list = previous_a

    print(f'Part 2: {min(previous_a)}')
