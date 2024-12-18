from run_util import run_puzzle
from collections import Counter

def parse_data(data):
    first_list, second_list = zip(*[map(int, line.split()) for line in data.splitlines()])
    return list(first_list), list(second_list)


def part_a(data):
    list1, list2 = parse_data(data)
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    return sum(abs(list1_sorted[i] - list2_sorted[i]) for i in range(len(list1)))

def part_b(data):
    list1, list2 = parse_data(data)
    right_list_counts = Counter(list2)
    return sum(num * right_list_counts[num] for num in list1)

def main():
    examples = [
        ("""3   4
4   3
2   5
1   3
3   9
3   3
""", 11, 31)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()