from run_util import run_puzzle
from utils.solution_base import SolutionBase
from collections import deque
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
            button_value = sum(2**i for i in button_indices)
            button_schematics.append(button_value)
            
            rest = rest[end_idx+1:].strip()
            
        joltage_requirements = tuple(int(x) for x in rest[1:rest.index('}')].split(','))
        machines.append({
            'lights': light_diagram,
            'buttons': button_schematics,
            'joltage': joltage_requirements
        })

    return machines


def count_moves(machine):
    moves = {0: 0}
    
    for button in machine['buttons']:
        update = True

        while update:
            update = False

            for move in moves.copy():
                new_state = move ^ button

                if (new_state not in moves) or (moves[new_state] > moves[move] + 1):
                    moves[new_state] = moves[move] + 1
                    update = True

    return moves[machine['lights']]

def solve_b(machine):
    joltage_reqs = machine['joltage']

    start = tuple(0 for _ in joltage_reqs)
    moves = {start: 0}

    buttons = []
    for button in machine['buttons']:
        end = tuple(0 for _ in joltage_reqs)
        for idx, char in enumerate(f"{button:b}"[::-1]):
            if char == '1':
                end = end[:idx] + (1,) + end[idx+1:]
        buttons.append(end)

    change = True
    while change:
        change = False

        for move in moves:
            new_moves = moves.copy()
            
            for button in buttons:
                new_state = tuple(map(sum, zip(move, button)))


                if new_state not in moves or new_moves[new_state] > moves[move] + 1:
                    if all(new_state[i] <= joltage_reqs[i] for i in range(len(joltage_reqs))):
                        new_moves[new_state] = moves[move] + 1
                        change = True

            moves = new_moves
    return moves[joltage_reqs]

def part_a(data):
    machines = parse_data(data)
    total_moves = 0
    for machine in machines:
        total_moves += count_moves(machine)
    return total_moves


def part_b(data):
    machines = parse_data(data)
    total_moves = 0
    for machine in machines:
        total_moves += solve_b(machine)
        print(f"Machine solved in {total_moves} moves")
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