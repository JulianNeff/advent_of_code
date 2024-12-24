from collections import defaultdict
from run_util import run_puzzle

def parse_data(data):
    values, gates = {}, []
    for line in data.strip().splitlines():
        parts = line.split("->")
        if len(parts) == 2:
            gates.append((*parts[0].split(), parts[1].strip()))
        elif ":" in line:
            wire, value = line.split(":")
            values[wire.strip()] = int(value)
    return values, gates


def evaluate_gates(wire_values, gates):
    adj = defaultdict(list)
    in_degree = [2] * len(gates)
    operations = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y
    }
    
    for i, (input_a, op, input_b, output_wire) in enumerate(gates):
        for input_wire in (input_a, input_b):
            adj[input_wire].append(i)
            if input_wire in wire_values:
                in_degree[i] -= 1

    ready = [i for i, deg in enumerate(in_degree) if deg == 0]
    while ready:
        idx = ready.pop(0)
        input_a, op, input_b, output_wire = gates[idx]
        if input_a in wire_values and input_b in wire_values:
            wire_values[output_wire] = operations[op](wire_values[input_a], wire_values[input_b])
            for next_idx in adj[output_wire]:
                in_degree[next_idx] -= 1
                if in_degree[next_idx] == 0:
                    ready.append(next_idx)
    return wire_values


def find_gate_output(gates, a, b, op):
    return next((out_w for (in_a, gate_op, in_b, out_w) in gates if gate_op == op and {in_a, in_b} == {a, b}), None)


def swap_wires(gates):
    swapped, carry_in = [], None
    for i in range(45):
        idx_str = f"{i:02d}"
        xor_wire = find_gate_output(gates, f"x{idx_str}", f"y{idx_str}", 'XOR')
        and_wire = find_gate_output(gates, f"x{idx_str}", f"y{idx_str}", 'AND')
        if carry_in:
            r_wire = find_gate_output(gates, carry_in, xor_wire, 'AND') or and_wire
            xor_wire, and_wire = (and_wire, xor_wire) if not r_wire else (xor_wire, and_wire)
            swapped.extend([xor_wire, and_wire])
            sum_wire = find_gate_output(gates, carry_in, xor_wire, 'XOR')
            swapped.extend([sum_wire, wire] for wire in (xor_wire, and_wire, r_wire) if wire and wire.startswith('z'))
            c_out_wire = find_gate_output(gates, r_wire, and_wire, 'OR')
            if c_out_wire and c_out_wire.startswith('z') and c_out_wire != 'z45':
                swapped.append([sum_wire, c_out_wire])
            carry_in = c_out_wire if carry_in else and_wire
        else:
            carry_in = and_wire
    return swapped


def part_a(data):
    wire_values, gates = parse_data(data)
    wire_values = evaluate_gates(wire_values, gates)
    return int(''.join(str(wire_values.get(f'z{i:02d}', 0)) for i in range(45))[::-1], 2)


def part_b(data):
    _, gates = parse_data(data)
    swapped = swap_wires(gates)
    flattened = [item for sublist in swapped for item in (sublist if isinstance(sublist, list) else [sublist])]
    return ",".join(sorted(set(filter(None, flattened))))


def main():
    examples = [
        ("""x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
""", 4, None),
        ("""x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""", 2024, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()