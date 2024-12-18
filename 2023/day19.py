from run_util import run_puzzle
import re


def parse_data(data):
    flows_section, parts_section = data.split('\n\n')

    extracted_parts = [list(map(int, re.findall(r'\d+', line))) for line in parts_section.split("\n")]
    extracted_flows = {line.split("{")[0]: line.split("{")[1][:-1] for line in flows_section.split("\n")}

    return extracted_flows, extracted_parts


def evaluate_condition(part, work, flow):
    work_flow = flow[work]
    x, m, a, s = part
    
    for item in work_flow.split(","):
        if item == "R":
            return False
        if item == "A":
            return True
        if ":" not in item:
            return evaluate_condition(part, item, flow)
        
        condition, result = item.split(":")
        if eval(condition):
            if result == "R":
                return False
            if result == "A":
                return True
            return evaluate_condition(part, result, flow)


def part_a(data):
    extracted_flows, extracted_parts = parse_data(data)

    total_sum = 0
    for part_data in extracted_parts:
        if evaluate_condition(part_data, 'in', extracted_flows):
            total_sum += sum(part_data)
            
    return total_sum


def adjust_ranges(character, greater_than, value, ranges):
    index = 'xmas'.index(character)
    updated_ranges = []

    for r in ranges:
        r = list(r)
        low, high = r[index]

        if greater_than:
            low = max(low, value + 1)
        else:
            high = min(high, value - 1)

        if low > high:
            continue

        r[index] = (low, high)
        updated_ranges.append(tuple(r))

    return updated_ranges


def get_range(sequence, flow):
    current = sequence[0]

    if current == "R":
        return []
    if current == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]

    if ":" not in current:
        return get_range(flow[current].split(","), flow)

    condition = current.split(":")[0]
    greater_than = ">" in condition
    value = int(condition[2:])
    inverted_value = value + 1 if greater_than else value - 1

    greater = adjust_ranges(condition[0], greater_than, value, get_range([current.split(":")[1]], flow))
    lesser = adjust_ranges(condition[0], not greater_than, inverted_value, get_range(sequence[1:], flow))

    return greater + lesser


def part_b(data):
    flow, _ = parse_data(data)

    total_product = 0
    for calculated_range in get_range(flow["in"].split(","), flow):
        product = 1
        
        for low, high in calculated_range:
            product *= high - low + 1
        
        total_product += product
    
    return total_product


def main():
    examples = [
        ("""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""", 19114, 167409079868000)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()