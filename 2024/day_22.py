from run_util import run_puzzle
from collections import defaultdict


def parse_data(data):
    return list(map(int, data.split('\n')))


def transform_sequence(value):
    mask = 0xFFFFFF
    value ^= (value << 6) & mask
    value ^= (value >> 5) & mask
    return value ^ ((value << 11) & mask)


def part_a(data):
    numbers = parse_data(data)
    for _ in range(2000):
        numbers = [transform_sequence(value) for value in numbers]
    return sum(numbers)


def part_b(data):
    pattern_scores = defaultdict(int)
    
    for initial_value in parse_data(data):
        sequence = [initial_value]
        for _ in range(2000):
            sequence.append(transform_sequence(sequence[-1]))
        
        differences = [(sequence[i] % 10) - (sequence[i - 1] % 10) for i in range(1, len(sequence))]
        seen_patterns = set()
        
        for idx in range(len(differences) - 3):
            pattern = tuple(differences[idx:idx + 4])
            if pattern not in seen_patterns:
                seen_patterns.add(pattern)
                pattern_scores[pattern] += sequence[idx + 4] % 10
    
    return max(pattern_scores.values())


def main():
    examples = [
        ("""1
10
100
2024""", 37327623, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()