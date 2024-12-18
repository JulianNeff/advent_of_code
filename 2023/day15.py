from run_util import run_puzzle


def get_hash(string : str, curr: int = 0) -> int:
    for c in string:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr


def calculate_total(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += int(box[lens]) * (1+i) * (1+j)
    return total


def part_a(data) -> int:
    return sum([get_hash(step) for step in data.split(',')])


def part_b(data):
    boxes = [{} for _ in range(256)]

    steps = data.split(',')
    for step in steps:
        if '=' in step:
            lens, focal_length = step.split('=')
            boxes[get_hash(lens)][lens] = focal_length
        else:
            lens = step[:-1]
            if lens in boxes[get_hash(lens)]:
                boxes[get_hash(lens)].pop(lens)

    return calculate_total(boxes)


def main():
    examples = [
        ("""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""", 1320, 145)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()