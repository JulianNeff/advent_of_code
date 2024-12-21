from typing import List
import numpy as np
from itertools import permutations
from run_util import run_puzzle


def is_valid_path(path: tuple, start: np.ndarray, restricted: np.ndarray, directions: dict) -> bool:
    position = start.copy()
    for step in path:
        position = position + directions[step]
        if np.array_equal(position, restricted):
            return False
    return True


def generate_valid_paths(start: np.ndarray, target: np.ndarray, restricted: np.ndarray) -> List[str]:
    displacement = target - start
    steps = []
    steps.extend(['^'] * -displacement[0] if displacement[0] < 0 else ['v'] * displacement[0])
    steps.extend(['<'] * -displacement[1] if displacement[1] < 0 else ['>'] * displacement[1])
    
    directions = {'^': np.array([-1, 0]), 'v': np.array([1, 0]),
                  '<': np.array([0, -1]), '>': np.array([0, 1])}
    
    valid_paths = []
    for path in set(permutations(steps)):
        if is_valid_path(path, start, restricted, directions):
            valid_paths.append(''.join(path) + 'a')
    
    return valid_paths or ['a']


def find_min_moves(sequence: str, max_depth: int, current_depth: int = 0) -> int:
    memo_key = (sequence, current_depth, max_depth)
    if memo_key in memoized_lengths:
        return memoized_lengths[memo_key]
    
    keypad_positions = {
        '7': np.array([0, 0]), '8': np.array([0, 1]), '9': np.array([0, 2]),
        '4': np.array([1, 0]), '5': np.array([1, 1]), '6': np.array([1, 2]),
        '1': np.array([2, 0]), '2': np.array([2, 1]), '3': np.array([2, 2]),
        '0': np.array([3, 1]), 'A': np.array([3, 2]),
        '^': np.array([0, 1]), 'a': np.array([0, 2]),
        '<': np.array([1, 0]), 'v': np.array([1, 1]), '>': np.array([1, 2])
    }
    
    restricted_position = np.array([3, 0]) if current_depth == 0 else np.array([0, 0])
    current_position = keypad_positions['A'] if current_depth == 0 else keypad_positions['a']
    total_moves = 0

    for char in sequence:
        next_position = keypad_positions[char]
        move_options = generate_valid_paths(current_position, next_position, restricted_position)

        if current_depth < max_depth:
            min_moves = min(
                (find_min_moves(moves, max_depth, current_depth + 1) for moves in move_options),
                default=float('inf')
            )
            total_moves += min_moves if min_moves < float('inf') else len(min(move_options, key=len))
        else:
            total_moves += len(min(move_options, key=len))

        current_position = next_position

    memoized_lengths[memo_key] = total_moves
    return total_moves


def solve_puzzle(data: str, is_part_a: bool) -> int:
    codes = [line.strip() for line in data.splitlines()]
    depth_limit = 2 if is_part_a else 25
    return sum([find_min_moves(code, depth_limit) * int(''.join(filter(str.isdigit, code))) for code in codes])


memoized_lengths = {}


def part_a(data: str) -> int:
    return solve_puzzle(data, is_part_a=True)


def part_b(data: str) -> int:
    return solve_puzzle(data, is_part_a=False)



def main():
    examples = [
        ("""029A
980A
179A
456A
379A""", 126384, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()