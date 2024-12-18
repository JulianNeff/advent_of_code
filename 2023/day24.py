from run_util import run_puzzle

import z3


def parse_input(data):
    return [[int(x) for x in line.replace('@', ',').replace(' ', '').split(',')] for line in data.splitlines()]


def part_a(data):
    hs = parse_input(data)

    min_test, max_test = (7, 27) if len(hs) == 5 else (200000000000000, 400000000000000)
    
    count = 0
    for i, hsi in enumerate(hs):
        s_i = hsi[4] / hsi[3]

        for j in range(i + 1, len(hs)):
            s_j = hs[j][4] / hs[j][3]

            if s_i == s_j:
                continue
            
            i_i = hsi[1] - s_i * hsi[0]
            i_j = hs[j][1] - s_j * hs[j][0]

            ix = (i_j - i_i) / (s_i - s_j)
            if (ix - hsi[0]) / hsi[3] < 0 or (ix - hs[j][0]) / hs[j][3] < 0:
                continue

            if min_test <= ix <= max_test and min_test <= s_i * ix + i_i <= max_test:
                count += 1

    return count


def part_b(data):
    hs = parse_input(data)

    pxr, pyr, pzr = z3.BitVecs("pxr pyr pzr", 64)
    vxr, vyr, vzr = z3.BitVecs("vxr vyr vzr", 64)

    solver = z3.Solver()

    for k, h in enumerate(hs[:3]):
        tK = z3.BitVec(f"t{k}", 64)
        solver.add(tK >= 0)
        solver.add(pxr + tK * vxr == h[0] + tK * h[3])
        solver.add(pyr + tK * vyr == h[1] + tK * h[4])
        solver.add(pzr + tK * vzr == h[2] + tK * h[5])

    solver.check()

    return sum(solver.model()[var].as_long() for var in [pxr, pyr, pzr])


def main():
    examples = [
        ("""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""", 2, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()