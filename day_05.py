from run_util import run_puzzle

def parse_data(data):
    rules_part, lists_part = data.split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules_part.splitlines()]
    lists = [list(map(int, line.split(","))) for line in lists_part.splitlines()]
    return rules, lists

def is_ordered(list, rules):
    for i, x in enumerate(list):
        for j, y in enumerate(list):
            if j <= i:
                continue
            if not (x, y) in rules:
                return False
    return True


def part_a(data):
    rules, lists = parse_data(data)
    count = 0
    for list in lists:
        if is_ordered(list, rules):
            count += list[len(list) // 2]
    return count


def part_b(data):
    rules, lists = parse_data(data)
    count = 0
    for list in lists:
        if is_ordered(list, rules):
            continue
        while not is_ordered(list, rules):
            for i in range(len(list)):
                for j in range(i+1, len(list)):
                    if (list[j], list[i]) in rules:
                        list[j], list[i] = list[i], list[j]
        count += list[len(list) // 2]
    return count


def main():
    examples = [
        ("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""", 143, 123)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()