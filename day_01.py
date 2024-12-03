from run_util import run_puzzle
from collections import Counter

def parse_data(data):
    list1, list2 = [], []

    for line in data.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    return list1, list2

def part_a(data):
    list1, list2 = parse_data(data)
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    return sum(abs(a - b) for a, b in zip(list1_sorted, list2_sorted))

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