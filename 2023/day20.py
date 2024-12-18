from run_util import run_puzzle
import math


def parse_data(data):
    lines = []
    for line in data.split("\n"):
        src, tar = line.split(" -> ")
        flip_flop = src.startswith("%")
        conjunction = src.startswith("&")
        state = None

        if flip_flop:
            state = False
            src = src[1:]

        if conjunction:
            state = {}
            src = src[1:]

        lines.append((src, [tar.split(", "), flip_flop, conjunction, state]))

    mappings = {key: value for key, value in lines}

    for key, value in mappings.items():
        if value[2]:
            for k, v in mappings.items():
                if key in v[0]:
                    value[3][k] = False

    return mappings


def step(curr_state, signal, input_signal, queue, mappings):
    targets, is_flip_flop, is_conjunction, state = mappings[curr_state]

    if is_flip_flop:
        if not signal:
            if state:
                mappings[curr_state][3] = False
                new_signal = 0
            else:
                mappings[curr_state][3] = True
                new_signal = 1

            for target in targets:
                queue.append((target, new_signal, curr_state))
    elif is_conjunction:
        state[input_signal] = bool(signal)
        if all(state.values()):
            new_signal = 0
        else:
            new_signal = 1
        for target in targets:
            queue.append((target, new_signal, curr_state))
    else:
        for target in targets:
            queue.append((target, signal, curr_state))


def part_a(data):
    mappings = parse_data(data)
    low_count = 0
    high_count = 0

    for _ in range(1000):
        queue = [("broadcaster", 0, None)]

        while queue:
            curr_state, signal, input_signal = queue.pop(0)

            if signal:
                high_count += 1
            else:
                low_count += 1

            if curr_state not in mappings:
                continue

            step(curr_state, signal, input_signal, queue, mappings)

    return low_count * high_count


def part_b(data):
    mappings = parse_data(data)

    lowest_parents = {
        "js": None,
        "zb": None,
        "bs": None,
        "rr": None,
    }

    curr_cycle = 0
    while True:
        queue = [("broadcaster", 0, None)]
        while queue:
            curr_state, signal, input_signal = queue.pop(0)

            if curr_state in lowest_parents and not signal:
                lowest_parents[curr_state] = curr_cycle

            if curr_state in mappings:
                step(curr_state, signal, input_signal, queue, mappings)

        curr_cycle += 1

        if all(val is not None for val in lowest_parents.values()):
            lowest_parents_cycles = list(lowest_parents.values())
            return math.lcm(*lowest_parents_cycles)



def main():
    examples = [
        ("""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""", 32000000, None),
("""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""", 11687500, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()