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


def part_2(input_string: str) -> int:
    known = dict([(s.split(': ')[0], int(s.split(': ')[1])) for s in input_string.split('\n\n')[0].split('\n')])
    connections = [(s.split(' ')[0], s.split(' ')[1], s.split(' ')[2], s.split(' ')[4])
                   for s in input_string.split('\n\n')[1].split('\n')]

    indices = sorted(set([x[0][1:] for x in [c for c in connections if c[0][0] == 'x' or c[2][0] == 'x']]))

    def out_wire(x: str, gate: str, y: str):
        return [c[3] for c in connections if (c[0] == x and c[1] == gate and c[2] == y) or
                (c[0] == y and c[1] == gate and c[2] == x)][0]

    result = [out_wire('x00', 'XOR', 'y00')]
    carry = [out_wire('x00', 'AND', 'y00')]

    for i in indices[1:]:
        res = out_wire(f'x{i}', 'XOR', f'y{i}')
        res = out_wire(res, 'XOR', carry[-1])
        car = out_wire(f'x{i}', 'XOR', f'y{i}')
        car = out_wire(car, 'AND', carry[-1])
        car = out_wire(car, 'OR', out_wire(f'x{i}', 'AND', f'y{i}'))
        result.append(res)
        carry.append(car)


if __name__ == '__main__':
    with open('../../data/input/24.txt', 'r') as f:
        string = f.read().strip()

    # string = ('x00: 1\nx01: 0\nx02: 1\nx03: 1\nx04: 0\ny00: 1\ny01: 1\ny02: 1\ny03: 1\ny04: 1\n\n'
    #           'ntg XOR fgs -> mjb\ny02 OR x01 -> tnw\nkwq OR kpj -> z05\nx00 OR x03 -> fst\ntgd XOR rvg -> z01\n'
    #           'vdt OR tnw -> bfw\nbfw AND frj -> z10\nffh OR nrd -> bqk\ny00 AND y03 -> djm\ny03 OR y00 -> psh\n'
    #           'bqk OR frj -> z08\ntnw OR fst -> frj\ngnj AND tgd -> z11\nbfw XOR mjb -> z00\nx03 OR x00 -> vdt\n'
    #           'gnj AND wpb -> z02\nx04 AND y00 -> kjc\ndjm OR pbm -> qhw\nnrd AND vdt -> hwm\nkjc AND fst -> rvg\n'
    #           'y04 OR y02 -> fgs\ny01 AND x02 -> pbm\nntg OR kjc -> kwq\npsh XOR fgs -> tgd\nqhw XOR tgd -> z09\n'
    #           'pbm OR djm -> kpj\nx03 XOR y03 -> ffh\nx00 XOR y04 -> ntg\nbfw OR bqk -> z06\nnrd XOR fgs -> wpb\n'
    #           'frj XOR qhw -> z04\nbqk OR frj -> z07\ny03 OR x01 -> nrd\nhwm AND bqk -> z03\ntgd XOR rvg -> z12\n'
    #           'tnw OR pbm -> gnj')

    print(f'part 1: {part_1(string)}')

    print(f'part 2: {part_2(string)}')
