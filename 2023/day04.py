from run_util import run_puzzle


def part_a(data):
    lines = data.split('\n')
    
    result = 0
    for line in lines:
        winners, numbers = line.split(':')[1].split('|')

        wins = set(win for win in winners.split())
        nums = set(num for num in numbers.split())

        matches = len(nums.intersection(wins))
        result += 2 ** (matches - 1) if matches > 0 else 0

    return result


def part_b(data):
    lines = data.split('\n')

    result = 0
    cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        winners, numbers = line.split(':')[1].split('|')

        wins = set(win for win in winners.split())
        nums = set(num for num in numbers.split())

        matches = len(nums.intersection(wins))

        for j in range(i+1, i+matches+1):
            cards[j] += cards[i]
        
        result += cards[i]

    return result


def main():
    examples = [
        ("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""", 13, None),
("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""", None, 30)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()