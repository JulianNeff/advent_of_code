from run_util import run_puzzle

def parse_data(data):
    lines = data.splitlines()
    a = int(lines[0].split(":")[1])
    b = int(lines[1].split(":")[1])
    c = int(lines[2].split(":")[1])
    program = list(map(int, lines[4].split(":")[1].split(",")))
    return a, b, c, program


def run(a, b, c, program):
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode, operand = program[instruction_pointer], program[instruction_pointer + 1]
        instruction_pointer += 2

        value = operand if operand < 4 else (a if operand == 4 else (b if operand == 5 else c))

        if opcode == 0:
            a = a // (2 ** value)
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = value % 8
        elif opcode == 3 and a > 0:
            instruction_pointer = operand
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            output.append(value % 8)
        elif opcode == 6:
            b = a // (2 ** value)
        elif opcode == 7:
            c = a // (2 ** value)

    return output


def part_a(data):
    a, b, c, program = parse_data(data)
    return ",".join(map(str, run(a, b, c, program)))


def find_matching_input(program, cursor, current_input):
    for candidate in range(8):
        next_input = current_input * 8 + candidate
        if run(next_input, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return next_input
            result = find_matching_input(program, cursor - 1, next_input)
            if result is not None:
                return result
    return None


def part_b(data):
    _, _, _, program = parse_data(data)
    return find_matching_input(program, len(program) - 1, 0)


def main():
    examples = [
        ("""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""", "4,6,3,5,6,3,5,2,1,0", None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()