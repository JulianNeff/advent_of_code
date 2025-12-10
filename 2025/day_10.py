from run_util import run_puzzle
from z3 import Optimize, Int, Sum, sat


def parse_data(data):
    lines = data.splitlines()

    machines = []
    for line in lines:
        light_diagram = line[line.index('[')+1:line.index(']')]
        light_diagram = int(''.join('1' if c == '#' else '0' for c in light_diagram[::-1]), 2)

        rest = line[line.index(']')+1:].strip()

        button_schematics = []
        while rest.startswith('('):
            end_idx = rest.index(')')

            button_spec = rest[1:end_idx]
            button_indices = [int(x) for x in button_spec.split(',')]
            button_schematics.append(button_indices)
            
            rest = rest[end_idx+1:].strip()
            
        joltage_requirements = tuple(int(x) for x in rest[1:rest.index('}')].split(','))
        machines.append({
            'lights': light_diagram,
            'buttons': button_schematics,
            'joltage': joltage_requirements
        })

    return machines
    

def part_a(data):
    machines = parse_data(data)
    total_moves = 0
    
    for machine in machines:
        moves = {0: 0}
        buttons = [sum(2**i for i in button) for button in machine['buttons']]

        for button in buttons:
            update = True

            while update:
                update = False

                for move in moves.copy():
                    new_state = move ^ button

                    if (new_state not in moves) or (moves[new_state] > moves[move] + 1):
                        moves[new_state] = moves[move] + 1
                        update = True

        total_moves += moves[machine['lights']]
    return total_moves


def part_b(data):
    machines = parse_data(data)
    total_moves = 0
    opt = Optimize()

    for machine in machines:
        opt.push()
        vars = [Int(f"x_{i}") for i in range(len(machine["buttons"]))]
        for v in vars: opt.add(v >= 0)

        for i, j in enumerate(machine["joltage"]):
            opt.add(Sum(vars[k] for k, b in enumerate(machine["buttons"]) if i in b) == j)

        opt.minimize(Sum(vars))
        if opt.check() != sat: raise ValueError("No solution found")

        m = opt.model()
        total_moves += sum(m[v].as_long() for v in vars)
        opt.pop()
    return total_moves


def main():
    examples = [
        ("""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""", 7, 33)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()