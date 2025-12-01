def part_1(input_string: str) -> int:
    known = dict([(s.split(': ')[0], int(s.split(': ')[1])) for s in input_string.split('\n\n')[0].split('\n')])
    connections = [(s.split(' ')[0], s.split(' ')[1], s.split(' ')[2], s.split(' ')[4])
                   for s in input_string.split('\n\n')[1].split('\n')]

    while connections:
        for a, gate, b, c in connections:
            if a in known and b in known:
                if gate == 'AND':
                    known[c] = known[a] & known[b]
                elif gate == 'OR':
                    known[c] = known[a] | known[b]
                elif gate == 'XOR':
                    known[c] = known[a] ^ known[b]
                connections.remove((a, gate, b, c))

    zk = sorted([k for k in known if k[0] == 'z'])
    digit_str = ''
    for k in zk:
        digit_str += str(known[k])

    return int(digit_str[::-1], base=2)


def part_2(input_string: str) -> str:
    connections = [(s.split(' ')[0], s.split(' ')[1], s.split(' ')[2], s.split(' ')[4])
                   for s in input_string.split('\n\n')[1].split('\n')]

    indices = sorted(set([x[0][1:] for x in [c for c in connections if c[0][0] == 'x' or c[2][0] == 'x']]))

    def out_wire(x: str, gate: str, y: str) -> str:
        return [c[3] for c in connections if (c[0] == x and c[1] == gate and c[2] == y) or
                (c[0] == y and c[1] == gate and c[2] == x)][0]

    def swap_outputs(s1: str, s2: str) -> None:
        tup1 = [c for c in connections if c[3] == s1][0]
        tup2 = [c for c in connections if c[3] == s2][0]
        idx_1 = connections.index(tup1)
        idx_2 = connections.index(tup2)
        tup1 = (tup1[0], tup1[1], tup1[2], s2)
        tup2 = (tup2[0], tup2[1], tup2[2], s1)
        connections[idx_1] = tup1
        connections[idx_2] = tup2

    result = [out_wire('x00', 'XOR', 'y00')]
    carry = [out_wire('x00', 'AND', 'y00')]

    for i in indices[1:]:
        res = out_wire(f'x{i}', 'XOR', f'y{i}')
        try:
            res = out_wire(res, 'XOR', carry[-1])
        except IndexError:
            s_1 = res
            if len([c for c in connections if c[1] == 'XOR' and c[0] == carry[-1]]) > 0:
                s_2 = [c[2] for c in connections if c[1] == 'XOR' and c[0] == carry[-1]][0]
                swap_outputs(s_1, s_2)
            elif len([c for c in connections if c[1] == 'XOR' and c[2] == carry[-1]]) > 0:
                s_2 = [c[0] for c in connections if c[1] == 'XOR' and c[2] == carry[-1]][0]
                swap_outputs(s_1, s_2)
            res = out_wire(s_2, 'XOR', carry[-1])
        if res != f'z{i}':
            swap_outputs(res, f'z{i}')
            res = f'z{i}'
        car = out_wire(f'x{i}', 'XOR', f'y{i}')
        try:
            car = out_wire(car, 'AND', carry[-1])
        except IndexError:
            s_1 = car
            if len([c for c in connections if c[1] == 'AND' and c[0] == carry[-1]]) > 0:
                s_2 = [c[2] for c in connections if c[1] == 'AND' and c[0] == carry[-1]][0]
                swap_outputs(s_1, s_2)
            elif len([c for c in connections if c[1] == 'AND' and c[2] == carry[-1]]) > 0:
                s_2 = [c[0] for c in connections if c[1] == 'AND' and c[2] == carry[-1]][0]
                swap_outputs(s_1, s_2)
            car = out_wire(s_2, 'AND', carry[-1])
        try:
            car = out_wire(car, 'OR', out_wire(f'x{i}', 'AND', f'y{i}'))
        except IndexError:
            s_1 = car
            if len([c for c in connections if c[1] == 'OR' and c[0] == out_wire(f'x{i}', 'AND', f'y{i}')]) > 0:
                s_2 = [c[2] for c in connections if c[1] == 'OR' and c[0] == out_wire(f'x{i}', 'AND', f'y{i}')][0]
                swap_outputs(s_1, s_2)
            elif len([c for c in connections if c[1] == 'OR' and c[2] == out_wire(f'x{i}', 'AND', f'y{i}')]) > 0:
                s_2 = [c[0] for c in connections if c[1] == 'OR' and c[2] == out_wire(f'x{i}', 'AND', f'y{i}')][0]
                swap_outputs(s_1, s_2)
            car = out_wire(s_2, 'OR', out_wire(f'x{i}', 'AND', f'y{i}'))
        result.append(res)
        carry.append(car)

    old_connections = [(s.split(' ')[0], s.split(' ')[1], s.split(' ')[2], s.split(' ')[4])
                       for s in input_string.split('\n\n')[1].split('\n')]

    swaps = []
    diff = set(connections).symmetric_difference(set(old_connections))
    diff = list(diff)
    for i in range(len(diff) - 1):
        for j in range(i + 1, len(diff)):
            tup_1 = diff[i]
            tup_2 = diff[j]
            if tup_1[0] == tup_2[0] and tup_1[1] == tup_2[1] and tup_1[2] == tup_2[2]:
                swaps.append(tup_1[3])
                swaps.append(tup_2[3])

    return ','.join(sorted(set(swaps)))


if __name__ == '__main__':
    with open('../../data/2024/24.txt', 'r') as f:
        string = f.read().strip()

    print(f'part 1: {part_1(string)}')

    print(f'part 2: {part_2(string)}')
